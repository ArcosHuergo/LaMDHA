from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.laboratorio_service import LaboratorioService
from app.mappers.zone.laboratorio_mapper import LaboratorioMapper

router = APIRouter()
laboratorio_service = LaboratorioService()

@router.get("/laboratorio/", tags=["Laboratorio"])
def obtener_todos_los_laboratorios():
    return LaboratorioMapper.to_schema_list(laboratorio_service.obtener_todos_los_laboratorios())

@router.get("/laboratorio/{id}", tags=["Laboratorio"])
def obtener_laboratorio_por_id(id: int):
    return LaboratorioMapper.to_schema(laboratorio_service.obtener_laboratorio_por_id(id))