from fastapi import APIRouter, HTTPException, Request, status

from app.mappers.log.registro_mapper import RegistroMapper
from app.schemas.log.registro_feedback import RegistroFeedbackSchema
from app.schemas.log.registro_completo import RegistroCompletoSchema
from app.services.log.registro_service import (
    RegistroAjenoError,
    RegistroNoEncontradoError,
    RegistroService,
)
from app.services.security.usuario_service import UsuarioService

router = APIRouter(prefix="/registro", tags=["Registro"])
usuario_service = UsuarioService()
registro_service = RegistroService()

@router.patch("/{id}/feedback", response_model=RegistroFeedbackSchema)
def actualizar_feedback(id: int, feedback: RegistroFeedbackSchema, request: Request):
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado.")

    try:
        registro = registro_service.actualizar_prediccion_correcta(usuario, id, feedback.prediccion_correcta)
    except RegistroNoEncontradoError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El registro no existe.")
    except RegistroAjenoError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="El registro pertenece a otro usuario.")

    return RegistroMapper.to_schema(registro)

@router.get("/feedback", response_model=list[RegistroCompletoSchema])
def obtener_registros_por_usuario(request: Request):
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado.")

    try:
        registros = registro_service.obtener_registros_por_usuario(usuario)
    except RegistroNoEncontradoError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El registro no existe.")

    return RegistroMapper.to_schema_completo_list(registros)