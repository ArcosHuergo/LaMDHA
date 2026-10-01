"""
Test de la lógica de parseo del cliente de Roboflow, usando como fixture la
respuesta REAL capturada al correr el workflow "lamdha" (versión corregida,
model_id "lamdha/9") vía el MCP de Roboflow. No requiere red: valida que
`_parse_prediction` interpreta correctamente la forma real de la respuesta.

Correr con: uv run python tests/test_roboflow_service.py
(o, si pytest está instalado como dependencia de desarrollo:
uv run python -m pytest tests/test_roboflow_service.py -v)
"""

import math
import sys
from pathlib import Path

# Permite ejecutar el archivo directamente (uv run python tests/test_roboflow_service.py)
# sin depender de que "backend/" ya esté en PYTHONPATH.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.vision.roboflow_service import (
    RoboflowInferenceError,
    _parse_prediction,
)

# Respuesta real devuelta por `run_workflow` (lista con una entrada por
# imagen de entrada), capturada corriendo el workflow con model_id
# "lamdha/9" contra una imagen de prueba.
REAL_WORKFLOW_RESPONSE = [
    {
        "predictions": {
            "inference_id": "fd856ecc-987b-4468-ad28-240464f1a386",
            "time": 0.04082880588248372,
            "image": {"width": 1920, "height": 1080},
            "predictions": [
                {
                    "class": "Laboratorio-PB-Violeta-7",
                    "class_id": 0,
                    "confidence": 0.7642,
                }
            ],
            "top": "Laboratorio-PB-Violeta-7",
            "confidence": 0.7642,
            "prediction_type": "classification",
            "parent_id": "image",
            "root_parent_id": "image",
        },
        "inference_id": "fd856ecc-987b-4468-ad28-240464f1a386",
        "model_id": "lamdha/9",
    }
]

# Misma forma real, pero con varias clases por encima del umbral de
# confianza, para validar el parseo de alternativas.
REAL_WORKFLOW_RESPONSE_MULTI_CLASS = [
    {
        "predictions": {
            "inference_id": "fd856ecc-987b-4468-ad28-240464f1a386",
            "time": 0.0408,
            "image": {"width": 1920, "height": 1080},
            "predictions": [
                {
                    "class": "Laboratorio-PB-Violeta-7",
                    "class_id": 0,
                    "confidence": 0.7642,
                },
                {"class": "Pasillo-PB-Violeta", "class_id": 1, "confidence": 0.15},
                {"class": "Aula-P1-Gris-4", "class_id": 2, "confidence": 0.05},
            ],
            "top": "Laboratorio-PB-Violeta-7",
            "confidence": 0.7642,
            "prediction_type": "classification",
            "parent_id": "image",
            "root_parent_id": "image",
        },
        "inference_id": "fd856ecc-987b-4468-ad28-240464f1a386",
        "model_id": "lamdha/9",
    }
]


def test_parse_prediction_real_shape():
    prediction = _parse_prediction(REAL_WORKFLOW_RESPONSE)

    assert prediction.model_id == "lamdha/9"
    assert prediction.inference_id == "fd856ecc-987b-4468-ad28-240464f1a386"
    # Con una sola clase por encima del umbral, "predicciones" trae esa única
    # entrada, y es la clase ganadora.
    assert len(prediction.predicciones) == 1
    assert prediction.predicciones[0].clase == "Laboratorio-PB-Violeta-7"
    assert math.isclose(prediction.predicciones[0].confianza, 0.7642)


def test_parse_prediction_multi_class_ordenadas_ganadora_primero():
    prediction = _parse_prediction(REAL_WORKFLOW_RESPONSE_MULTI_CLASS)

    # La ganadora ("top") queda en predicciones[0] por tener mayor confianza,
    # en la misma lista que el resto de las clases — sin campos separados.
    assert [p.clase for p in prediction.predicciones] == [
        "Laboratorio-PB-Violeta-7",
        "Pasillo-PB-Violeta",
        "Aula-P1-Gris-4",
    ]
    confidencias = [p.confianza for p in prediction.predicciones]
    assert confidencias == sorted(confidencias, reverse=True)


def test_parse_prediction_sin_lista_interna_usa_top_como_red_de_seguridad():
    # Si falta la lista interna "predictions", igual se arma "predicciones"
    # con la clase ganadora a partir de "top"/"confidence" — el dato esencial
    # nunca se pierde aunque la lista interna venga incompleta.
    raw = [
        {
            "predictions": {"top": "Patio-P1-Amarillo", "confidence": 0.9},
            "model_id": "lamdha/9",
            "inference_id": "abc",
        }
    ]
    prediction = _parse_prediction(raw)
    assert len(prediction.predicciones) == 1
    assert prediction.predicciones[0].clase == "Patio-P1-Amarillo"
    assert math.isclose(prediction.predicciones[0].confianza, 0.9)


def test_parse_prediction_empty_results_raises():
    try:
        _parse_prediction([])
    except RoboflowInferenceError:
        return
    raise AssertionError("se esperaba RoboflowInferenceError")


def test_parse_prediction_missing_predictions_key_raises():
    try:
        _parse_prediction([{"model_id": "lamdha/9", "inference_id": "abc"}])
    except RoboflowInferenceError:
        return
    raise AssertionError("se esperaba RoboflowInferenceError")


def test_parse_prediction_sin_clases_validas_raises():
    # Ni lista interna de clases ni "top"/"confidence": no hay ninguna clase
    # que reportar, así que debe fallar en lugar de devolver algo vacío.
    try:
        _parse_prediction([{"predictions": {"model_id": "lamdha/9"}}])
    except RoboflowInferenceError:
        return
    raise AssertionError("se esperaba RoboflowInferenceError")


if __name__ == "__main__":
    # Permite correrlo sin pytest instalado: uv run python tests/test_roboflow_service.py
    test_parse_prediction_real_shape()
    test_parse_prediction_multi_class_ordenadas_ganadora_primero()
    test_parse_prediction_sin_lista_interna_usa_top_como_red_de_seguridad()
    test_parse_prediction_empty_results_raises()
    test_parse_prediction_missing_predictions_key_raises()
    test_parse_prediction_sin_clases_validas_raises()
    print("Todos los tests de parseo pasaron correctamente.")
