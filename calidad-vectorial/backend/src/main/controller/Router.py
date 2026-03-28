from fastapi import APIRouter
from controller import UsuarioController

api_router = APIRouter()
api_router.include_router(UsuarioController.router)