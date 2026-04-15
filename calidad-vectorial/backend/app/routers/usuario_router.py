from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from services.usuario_service import UsuarioService
from models.usuario import Usuario

router = APIRouter()

@router.get("/usuario", tags=["Usuario"])
def prueba():
    return JSONResponse(content="prueba de usuario")

@router.get("/usuario/{id}", tags=["Usuario"])
def obtener_usuario_por_id(id: int):
    return UsuarioService.obtener_usuario_por_id(id)

@router.post("/usuario", tags=["Usuario"])
def crear_usuario(usuario: Usuario) -> Usuario:
    return JSONResponse(content=UsuarioService.crear_usuario(usuario).model_dump())