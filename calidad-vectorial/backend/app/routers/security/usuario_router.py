from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.security.usuario_service import UsuarioService
from app.mappers.security.usuario_mapper import UsuarioMapper
from app.schemas.security.usuario_response import UsuarioResponseSchema

router = APIRouter(prefix="/usuario", tags=["Usuario"])
usuario_service = UsuarioService()

@router.get("", response_model = list[UsuarioResponseSchema])
def obtener_usuarios():
    return UsuarioMapper.to_schema_list(usuario_service.obtener_todos_los_usuarios())

@router.get("/{id}", response_model = UsuarioResponseSchema)
def obtener_usuario_por_id(id: int):
    return UsuarioMapper.to_schema(usuario_service.obtener_usuario_por_id(id))