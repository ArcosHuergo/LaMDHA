from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.laboratorio_service import LaboratorioService
from app.mappers.zone.laboratorio_mapper import LaboratorioMapper
from app.schemas.zone.laboratorio_response import LaboratorioResponseSchema

router = APIRouter(prefix = "/laboratorio", tags=["Laboratorio"])
laboratorio_service = LaboratorioService()

@router.get("", response_model = list[LaboratorioResponseSchema])
def obtener_laboratorios():
    return LaboratorioMapper.to_schema_list(laboratorio_service.obtener_todos_los_laboratorios())

@router.get("/{id}", response_model = LaboratorioResponseSchema)
def obtener_laboratorio_por_id(id: int):
    return LaboratorioMapper.to_schema(laboratorio_service.obtener_laboratorio_por_id(id))

@router.get("/nombre/{nombre}", response_model = LaboratorioResponseSchema)
def obtener_laboratorio_por_nombre(nombre: str):
    return LaboratorioMapper.to_schema(laboratorio_service.obtener_laboratorio_por_nombre(nombre))