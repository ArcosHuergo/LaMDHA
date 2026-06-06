from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.sector.zona_service import ZonaService

router = APIRouter()
service = ZonaService()

@router.get("/zona/", tags=["Zona"])
def obtener_zonas():
    return service.obtener_todos_las_zonas()

@router.get("/zona/{id}", tags=["Zona"])
def obtener_aula_por_id(id: int):
    return service.obtener_zona_por_id(id)
