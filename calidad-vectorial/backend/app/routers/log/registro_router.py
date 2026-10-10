from app.mappers.log.registro_mapper import RegistroMapper
from app.schemas.log.registro_completo import RegistroCompletoSchema
from app.schemas.log.registro_feedback import RegistroFeedbackSchema
from app.services.log.registro_service import (
    RegistroAjenoError,
    RegistroNoEncontradoError,
    RegistroService,
)
from app.services.security.usuario_service import UsuarioService
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import FileResponse

router = APIRouter(prefix="/registro", tags=["Registro"])
usuario_service = UsuarioService()
registro_service = RegistroService()


@router.patch("/feedback/{id}", response_model=RegistroFeedbackSchema)
def actualizar_feedback(id: int, feedback: RegistroFeedbackSchema, request: Request):
    """Actualiza la predicción correcta asociada a un registro del usuario.

    Args:

        id: Identificador del registro.
        feedback: Datos con la predicción correcta.
        request: Solicitud HTTP con la información del usuario autenticado.

    Returns:

        El registro actualizado convertido a su esquema de respuesta.

    Raises:

        HTTPException: Si el usuario no existe, el registro no existe o
            pertenece a otro usuario.
    """
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado."
        )

    try:
        registro = registro_service.actualizar_prediccion_correcta(
            usuario, id, feedback.prediccion_correcta
        )
    except RegistroNoEncontradoError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El registro no existe."
        )
    except RegistroAjenoError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El registro pertenece a otro usuario.",
        )

    return RegistroMapper.to_schema(registro)


@router.get("/feedback", response_model=list[RegistroCompletoSchema])
def obtener_registros_del_usuario(request: Request):
    """Obtiene todos los registros asociados al usuario autenticado.

    Args:

        request: Solicitud HTTP con la información del usuario autenticado.

    Returns:

        Lista de registros del usuario convertidos a sus esquemas de respuesta.

    Raises:

        HTTPException: Si el usuario no existe o no se encuentran registros.
    """
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado."
        )

    try:
        registros = registro_service.obtener_registros_por_usuario(usuario)
    except RegistroNoEncontradoError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El registro no existe."
        )

    return RegistroMapper.to_schema_completo_list(registros)


@router.get("/foto/{id}")
def obtener_foto(id: int, request: Request):
    """Obtiene la foto asociada a un registro del usuario autenticado.

    Args:

        id: Identificador del registro.
        request: Solicitud HTTP con la información del usuario autenticado.

    Returns:

        Respuesta HTTP con el archivo de imagen asociado al registro.

    Raises:
    
        HTTPException: Si el usuario no existe, el registro no existe,
            pertenece a otro usuario o no tiene una foto asociada.
    """
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado."
        )

    try:
        registro = registro_service.obtener_registro_por_id(usuario, id)
    except RegistroNoEncontradoError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El registro no existe."
        )
    except RegistroAjenoError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El registro pertenece a otro usuario.",
        )

    if registro.url_foto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El registro no tiene una foto asociada.",
        )

    return FileResponse(registro.url_foto)
