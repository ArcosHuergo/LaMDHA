from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.patio_service import PatioService
from app.mappers.zone.patio_mapper import PatioMapper

router = APIRouter()
patio_service = PatioService()

@router.get("/patio/", tags=["Patio"])
def obtener_patios():
    return PatioMapper.to_schema_list(patio_service.obtener_todos_los_patios())

@router.get("/patio/{id}", tags=["Patio"])
def obtener_patio_por_id(id: int):
    return PatioMapper.to_schema(patio_service.obtener_patio_por_id(id))