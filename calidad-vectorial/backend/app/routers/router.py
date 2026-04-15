from fastapi import APIRouter
from routers import usuario

api_router = APIRouter()
api_router.include_router(usuario.router)