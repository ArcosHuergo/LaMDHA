import base64

from fastapi import APIRouter, File, HTTPException, Request, UploadFile, status

from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.log.foto_storage_service import guardar_foto
from app.services.log.registro_service import RegistroService
from app.services.security.usuario_service import UsuarioService
from app.services.vision.roboflow_service import (RoboflowInferenceError, clasificar_ubicacion)

router = APIRouter(prefix="/vision", tags=["Vision"])
usuario_service = UsuarioService()
registro_service = RegistroService()

@router.post("/ubicacion", response_model=RoboflowPrediction)
async def clasificar_imagen_ubicacion(request: Request, imagen: UploadFile = File(...)) -> RoboflowPrediction:
    contenido = await imagen.read()
    imagen_base64 = base64.b64encode(contenido).decode("utf-8")

    try:
        prediction = clasificar_ubicacion(imagen_base64)
    except RoboflowInferenceError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"No se pudo clasificar la imagen: {error}",
        )

    try:
        usuario = usuario_service.obtener_usuario_por_username(request.state.username)
        url_foto = guardar_foto(contenido, imagen.filename or "foto.jpg")
        registro_service.registrar_clasificacion(usuario, url_foto, prediction)
    except AttributeError as error:
        pass

    return prediction