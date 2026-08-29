from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.aula_service import AulaService
from app.mappers.zone.aula_mapper import AulaMapper

router = APIRouter()
aula_service = AulaService()

@router.get("/aula/", tags=["Aula"])
def obtener_aulas():
    return AulaMapper.to_schema_list(aula_service.obtener_todas_las_aulas())

@router.get("/aula/{id}", tags=["Aula"])
def obtener_aula_por_id(id: int):
    return AulaMapper.to_schema(aula_service.obtener_aula_por_id(id))