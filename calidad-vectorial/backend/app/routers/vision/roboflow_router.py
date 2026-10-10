import base64
import logging

from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.log.foto_storage_service import guardar_foto
from app.services.log.registro_service import RegistroService
from app.services.security.usuario_service import UsuarioService
from app.services.vision.roboflow_service import (
    RoboflowInferenceError,
    clasificar_ubicacion,
)
from fastapi import APIRouter, File, HTTPException, Request, UploadFile, status

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/vision", tags=["Vision"])
usuario_service = UsuarioService()
registro_service = RegistroService()


@router.post("/ubicacion", response_model=RoboflowPrediction)
async def clasificar_imagen_ubicacion(
    request: Request, imagen: UploadFile = File(...)
) -> RoboflowPrediction:
    """Clasifica una imagen para determinar su ubicación.

    La imagen se convierte a Base64 y se envía al servicio de inferencia.
    Si existe un usuario autenticado, se almacena la imagen y el resultado
    de la clasificación como un registro.

    Args:

        request: Solicitud HTTP con la información del usuario autenticado.
        imagen: Imagen que se desea clasificar.

    Returns:

        Predicción obtenida a partir de la imagen.

    Raises:
    
        HTTPException: Si ocurre un error durante la inferencia de la imagen.
    """
    contenido = await imagen.read()
    imagen_base64 = base64.b64encode(contenido).decode("utf-8")

    try:
        prediction = clasificar_ubicacion(imagen_base64)
    except RoboflowInferenceError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"No se pudo clasificar la imagen: {error}",
        )

    username = getattr(request.state, "username", None)
    if username is not None:
        try:
            usuario = usuario_service.obtener_usuario_por_username(username)
            if usuario is not None:
                url_foto = guardar_foto(contenido, imagen.filename or "foto.jpg")
                registro = registro_service.registrar_clasificacion(
                    usuario, url_foto, prediction
                )
                prediction.registro_id = registro.id
        except Exception:
            logger.exception("No se pudo guardar el registro de la clasificación.")

    return prediction