from __future__ import annotations

import logging
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeoutError
from typing import Any

from inference_sdk import InferenceHTTPClient
from inference_sdk.http.entities import InferenceConfiguration
from inference_sdk.http.errors import HTTPClientError, HTTPCallErrorError

from app.config.settings import settings
from app.schemas.vision.roboflow_prediction import ClassPrediction, RoboflowPrediction

logger = logging.getLogger(__name__)

WORKSPACE_NAME = "ignacios-workspace"
WORKFLOW_ID = "lamdha"

DEFAULT_TIMEOUT_SECONDS = 10.0
DEFAULT_MAX_RETRIES = 2
DEFAULT_BACKOFF_BASE_SECONDS = 1.0


class RoboflowInferenceError(Exception):
    """Error de configuración, red o parseo al invocar el workflow de Roboflow."""


def _build_client() -> InferenceHTTPClient:
    if not settings.roboflow_api_key:
        raise RoboflowInferenceError(
            "ROBOFLOW_API_KEY no está configurada (ver .env / "
            "https://app.roboflow.com/settings/api)."
        )
    client = InferenceHTTPClient(
        api_url=settings.roboflow_api_url,
        api_key=settings.roboflow_api_key,
    )

    client.configure(InferenceConfiguration(workflow_run_retries_enabled=False))
    return client


def _parse_prediction(raw_results: list[dict[str, Any]]) -> RoboflowPrediction:
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


def _parse_predicciones(predictions_block: dict[str, Any]) -> list[ClassPrediction]:
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
            predicciones.append(ClassPrediction(clase=clase, confianza=float(confianza)))

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


def clasificar_ubicacion(
    image: Any,
    confidence: float = 0.4,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_retries: int = DEFAULT_MAX_RETRIES,
) -> RoboflowPrediction:
    
    client = _build_client()

    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(
                    client.run_workflow,
                    workspace_name=WORKSPACE_NAME,
                    workflow_id=WORKFLOW_ID,
                    images={"image": image},
                    parameters={"confidence": confidence},
                )
                raw_results = future.result(timeout=timeout)
            return _parse_prediction(raw_results)
        except FutureTimeoutError as error:
            last_error = error
            logger.warning(
                "Intento %s/%s: timeout (%ss) llamando al workflow '%s'.",
                attempt + 1, max_retries + 1, timeout, WORKFLOW_ID,
            )
        except (HTTPCallErrorError, HTTPClientError) as error:
            last_error = error
            logger.warning(
                "Intento %s/%s: error llamando al workflow '%s': %s",
                attempt + 1, max_retries + 1, WORKFLOW_ID, error,
            )

        if attempt < max_retries:
            time.sleep(DEFAULT_BACKOFF_BASE_SECONDS * (2 ** attempt))

    raise RoboflowInferenceError(
        f"Falló la llamada al workflow '{WORKFLOW_ID}' tras "
        f"{max_retries + 1} intento(s). Último error: {last_error}"
    ) from last_error
