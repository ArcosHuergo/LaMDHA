from fastapi import APIRouter
from app.routers import usuario_router

api_router = APIRouter()
api_router.include_router(usuario_router.router)