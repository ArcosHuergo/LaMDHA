from __future__ import annotations

import logging
import time
from typing import Any

import httpx
from app.config.settings import settings
from app.schemas.vision.roboflow_prediction import ClassPrediction, RoboflowPrediction

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT_SECONDS = 10.0
DEFAULT_MAX_RETRIES = 2
DEFAULT_BACKOFF_BASE_SECONDS = 1.0


class RoboflowInferenceError(Exception):
    """Error de configuración, red o parseo al invocar el workflow de Roboflow."""


def _run_workflow(
    image_base64: str, confidence: float, timeout: float
) -> list[dict[str, Any]]:
    """Ejecuta el workflow de Roboflow mediante su API HTTP.

    Args:
        image_base64: Imagen codificada en Base64.
        confidence: Umbral de confianza utilizado por el workflow.
        timeout: Tiempo máximo de espera, en segundos.

    Returns:
        Lista de resultados devuelta por el workflow.

    Raises:
        RoboflowInferenceError: Si falta la API key.
        httpx.HTTPError: Si falla la llamada HTTP.
    """
    if not settings.roboflow_api_key:
        raise RoboflowInferenceError("ROBOFLOW_API_KEY no está configurada.")

    url = (
        f"{settings.roboflow_api_url.rstrip('/')}/"
        f"{settings.workspace_name}/workflows/{settings.workflow_id}"
    )
    payload = {
        "api_key": settings.roboflow_api_key,
        "inputs": {
            "image": {"type": "base64", "value": image_base64},
            "confidence": confidence,
        },
    }
    response = httpx.post(url, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json().get("outputs", [])


def clasificar_ubicacion(
    image: Any,
    confidence: float = 0.4,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_retries: int = DEFAULT_MAX_RETRIES,
) -> RoboflowPrediction:
    """Clasifica una imagen mediante un workflow de Roboflow.

    Realiza la inferencia con un tiempo máximo de espera y reintenta
    automáticamente ante errores de red, timeout o errores del servidor.

    Args:
        image: Imagen en Base64 que se desea clasificar.
        confidence: Umbral de confianza utilizado por el workflow.
        timeout: Tiempo máximo de espera por intento, en segundos.
        max_retries: Cantidad máxima de reintentos después del primer intento.

    Returns:
        Predicción obtenida del workflow de Roboflow.

    Raises:
        RoboflowInferenceError: Si falla la configuración, la inferencia o
            el procesamiento de la respuesta después de los reintentos.
    """
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            raw_results = _run_workflow(image, confidence, timeout)
            return _parse_prediction(raw_results)
        except httpx.HTTPStatusError as error:
            last_error = error
            logger.warning(
                "Intento %s/%s: HTTP %s del workflow '%s': %s",
                attempt + 1,
                max_retries + 1,
                error.response.status_code,
                settings.workflow_id,
                error.response.text[:300],
            )
            # Los errores 4xx (key inválida, workflow inexistente) no se reintentan
            if error.response.status_code < 500:
                break
        except httpx.HTTPError as error:  # timeout, conexión, etc.
            last_error = error
            logger.warning(
                "Intento %s/%s: error de red llamando al workflow '%s': %r",
                attempt + 1,
                max_retries + 1,
                settings.workflow_id,
                error,
            )

        if attempt < max_retries:
            time.sleep(DEFAULT_BACKOFF_BASE_SECONDS * (2**attempt))

    raise RoboflowInferenceError(
        f"Falló la llamada al workflow '{settings.workflow_id}'. "
        f"Último error: {last_error}"
    ) from last_error


def _parse_prediction(raw_results: list[dict[str, Any]]) -> RoboflowPrediction:
    """Convierte la respuesta del workflow en una predicción.

    Args:
        raw_results: Resultados obtenidos del workflow de Roboflow.

    Returns:
        Predicción estructurada a partir de los resultados.

    Raises:
        RoboflowInferenceError: Si la respuesta no contiene datos válidos.
    """
    if not raw_results:
        raise RoboflowInferenceError("El workflow no devolvió resultados.")

    result = raw_results[0]
    predictions_block = result.get("predictions")
    if not isinstance(predictions_block, dict):
        raise RoboflowInferenceError(
            f"Respuesta del workflow con forma inesperada (sin 'predictions'). "
            f"Claves disponibles: {list(result.keys())}"
        )

    predicciones = _parse_predicciones(predictions_block)
    if not predicciones:
        raise RoboflowInferenceError(
            f"La respuesta de 'predictions' no trae ninguna clase válida "
            f"('predictions[]' vacío/ausente y sin 'top'/'confidence'). "
            f"Claves disponibles: {list(predictions_block.keys())}"
        )

    return RoboflowPrediction(
        predicciones=predicciones,
        model_id=result.get("model_id"),
        inference_id=result.get("inference_id"),
    )


def _parse_predicciones(
    predictions_block: dict[str, Any],
) -> list[ClassPrediction]:
    """Extrae y ordena las predicciones de la respuesta del workflow.

    Args:
        predictions_block: Bloque de predicciones devuelto por Roboflow.

    Returns:
        Lista de predicciones ordenadas por confianza descendente.
    """
    predicciones: list[ClassPrediction] = []

    raw_class_predictions = predictions_block.get("predictions")
    if isinstance(raw_class_predictions, list):
        for entry in raw_class_predictions:
            if not isinstance(entry, dict):
                continue
            clase = entry.get("class")
            confianza = entry.get("confidence")
            if clase is None or confianza is None:
                continue
            predicciones.append(
                ClassPrediction(clase=clase, confianza=float(confianza))
            )

    top = predictions_block.get("top")
    top_confianza = predictions_block.get("confidence")
    if (
        top is not None
        and top_confianza is not None
        and not any(p.clase == top for p in predicciones)
    ):
        predicciones.append(ClassPrediction(clase=top, confianza=float(top_confianza)))

    predicciones.sort(key=lambda p: p.confianza, reverse=True)
    return predicciones
