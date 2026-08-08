from fastapi import APIRouter
from app.routers.security import usuario_router, auth_router
from app.routers.sector import zona_router

api_router = APIRouter()
api_router.include_router(usuario_router.router)
api_router.include_router(auth_router.router)
api_router.include_router(zona_router.router)