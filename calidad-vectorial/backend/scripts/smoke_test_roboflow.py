"""
Smoke test EN VIVO del workflow "lamdha" contra la API de Roboflow.

Requiere:
  - ROBOFLOW_API_KEY configurada en el entorno o en backend/.env.
  - Que el workflow guardado "lamdha" en el workspace "ignacios-workspace"
    ya tenga corregido el model_id del paso de clasificación (ver la nota
    al principio de app/services/vision/roboflow_service.py — al momento de
    escribir esto, el workflow guardado todavía apunta al model_id viejo
    "ubicacion-huergo/6" y hay que corregirlo a mano en la UI de Roboflow).

Uso:
    uv run python scripts/smoke_test_roboflow.py
    uv run python scripts/smoke_test_roboflow.py --image /ruta/a/una/foto.jpg
"""

from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

# Permite ejecutar el script directamente (uv run python scripts/smoke_test_roboflow.py)
# sin depender de que "backend/" ya esté en PYTHONPATH.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.vision.roboflow_service import (
    RoboflowInferenceError,
    clasificar_ubicacion,
)

# Imagen pública de referencia, solo para verificar que el circuito completo
# (auth, red, workflow, parseo) funciona de punta a punta.
DEFAULT_TEST_IMAGE = "https://media.roboflow.com/inference/people-walking.jpg"


def _resolver_imagen(image_arg: str) -> str:
    """
    Si `image_arg` es una URL (http/https), se pasa tal cual — inference-sdk
    la maneja directamente. Si es un path local, se lee y se convierte a
    base64 acá mismo: pasarle el path crudo al SDK hace que lo cargue y lo
    convierta a un array de numpy del lado del cliente, y el endpoint
    serverless de Roboflow rechaza ese tipo de payload (solo acepta URL o
    base64), así que evitamos ese camino.
    """
    if image_arg.startswith("http://") or image_arg.startswith("https://"):
        return image_arg

    path = Path(image_arg)
    if not path.is_file():
        raise SystemExit(f"No se encontró el archivo de imagen: {path}")

    contenido = path.read_bytes()
    return base64.b64encode(contenido).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--image",
        default=DEFAULT_TEST_IMAGE,
        help="URL https o path local a una imagen de prueba.",
    )
    args = parser.parse_args()

    imagen = _resolver_imagen(args.image)

    print(f"Corriendo el workflow 'lamdha' contra: {args.image}")
    try:
        prediction = clasificar_ubicacion(imagen)
    except RoboflowInferenceError as error:
        print(f"FALLÓ: {error}", file=sys.stderr)
        return 1

    print(f"predicciones: {len(prediction.predicciones)} clase(s) por encima del umbral")
    for i, p in enumerate(prediction.predicciones):
        marca = " (ganadora)" if i == 0 else ""
        print(f"  [{i}] {p.clase} — confianza {p.confianza}{marca}")
    print(f"model_id:     {prediction.model_id}")
    print(f"inference_id: {prediction.inference_id}")

    assert prediction.predicciones, "se esperaba al menos una clase predicha"
    ganadora = prediction.predicciones[0]
    assert ganadora.clase, "se esperaba una clase ganadora no vacía"
    assert 0.0 <= ganadora.confianza <= 1.0, "confianza fuera de rango"

    print("OK: el smoke test pasó correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())