from fastapi import APIRouter
from app.routers.security import usuario_router, auth_router
from app.routers.sector import zona_router
from app.routers.log import registro_router
from app.routers.vision import roboflow_router
from app.routers.zone import aula_router, pasillo_router, patio_router, laboratorio_router, biblioteca_router

api_router = APIRouter()
api_router.include_router(auth_router.router)
api_router.include_router(usuario_router.router)
api_router.include_router(zona_router.router)
api_router.include_router(aula_router.router)
api_router.include_router(laboratorio_router.router)
api_router.include_router(pasillo_router.router)
api_router.include_router(patio_router.router)
api_router.include_router(biblioteca_router.router)
api_router.include_router(roboflow_router.router)
api_router.include_router(registro_router.router)