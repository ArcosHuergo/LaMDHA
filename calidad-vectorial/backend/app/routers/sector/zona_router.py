from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.sector.zona_service import ZonaService
from app.mappers.sector.zona_mapper import ZonaMapper
from app.schemas.sector.zona_response import ZonaResponseSchema

router = APIRouter(prefix = "/zona", tags=["Zona"])
zona_service = ZonaService()

@router.get("", response_model = list[ZonaResponseSchema])
def obtener_zonas():
    return ZonaMapper.to_schema_list(zona_service.obtener_todos_las_zonas())

@router.get("/{id}", response_model = ZonaResponseSchema)
def obtener_aula_por_id(id: int):
    return ZonaMapper.to_schema(zona_service.obtener_zona_por_id(id))
