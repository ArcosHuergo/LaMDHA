from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.security.usuario_service import UsuarioService

router = APIRouter()
service = UsuarioService()

@router.get("/usuario", tags=["Usuario"])
def prueba():
    return JSONResponse(content="prueba de usuario")

@router.get("/usuario/{id}", tags=["Usuario"])
def obtener_usuario_por_id(id: int):
    return service.obtener_usuario_por_id(id)