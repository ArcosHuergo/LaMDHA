from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.patio_service import PatioService
from app.mappers.zone.patio_mapper import PatioMapper
from app.schemas.zone.patio_response import PatioResponseSchema

router = APIRouter(prefix = "/patio", tags=["Patio"])
patio_service = PatioService()

@router.get("", response_model = list[PatioResponseSchema])
def obtener_patios():
    return PatioMapper.to_schema_list(patio_service.obtener_todos_los_patios())

@router.get("/{id}", response_model = PatioResponseSchema)
def obtener_patio_por_id(id: int):
    return PatioMapper.to_schema(patio_service.obtener_patio_por_id(id))

@router.get("/nombre/{nombre}", response_model = PatioResponseSchema)
def obtener_patio_por_nombre(nombre: str):
    return PatioMapper.to_schema(patio_service.obtener_patio_por_nombre(nombre))