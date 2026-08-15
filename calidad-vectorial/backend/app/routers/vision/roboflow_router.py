import base64

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.vision.roboflow_service import (
    RoboflowInferenceError,
    clasificar_ubicacion,
)

router = APIRouter(prefix="/vision", tags=["Vision"])

@router.post("/ubicacion", response_model=RoboflowPrediction)
async def clasificar_imagen_ubicacion(imagen: UploadFile = File(...)) -> RoboflowPrediction:
    contenido = await imagen.read()
    imagen_base64 = base64.b64encode(contenido).decode("utf-8")

    try:
        return clasificar_ubicacion(imagen_base64)
    except RoboflowInferenceError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"No se pudo clasificar la imagen: {error}",
        )