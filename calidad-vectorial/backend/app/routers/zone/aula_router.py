from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.aula_service import AulaService
from app.mappers.zone.aula_mapper import AulaMapper
from app.schemas.zone.aula_response import AulaResponseSchema

router = APIRouter(prefix = "/aula", tags=["Aula"])
aula_service = AulaService()

@router.get("", response_model = list[AulaResponseSchema])
def obtener_aulas():
    return AulaMapper.to_schema_list(aula_service.obtener_todas_las_aulas())

@router.get("/{id}", response_model = AulaResponseSchema)
def obtener_aula_por_id(id: int):
    return AulaMapper.to_schema(aula_service.obtener_aula_por_id(id))

@router.get("/nombre/{nombre}", response_model = AulaResponseSchema)
def obtener_aula_por_nombre(nombre: str):
    return AulaMapper.to_schema(aula_service.obtener_aula_por_nombre(nombre))