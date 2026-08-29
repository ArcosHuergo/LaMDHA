from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.laboratorio_service import LaboratorioService

router = APIRouter()
service = LaboratorioService()

@router.get("/laboratorio/", tags=["Laboratorio"])
def obtener_todos_los_laboratorios():
    return service.obtener_todos_los_laboratorios()

@router.get("/laboratorio/{id}", tags=["Laboratorio"])
def obtener_laboratorio_por_id(id: int):
    return service.obtener_laboratorio_por_id(id)