from fastapi import APIRouter, HTTPException, status

from app.services.sector.zona_service import ZonaService
from app.mappers.sector.zona_mapper import ZonaMapper
from app.schemas.sector.zona_response import ZonaResponseSchema

router = APIRouter(prefix = "/zona", tags=["Zona"])
zona_service = ZonaService()

@router.get("", response_model = list[ZonaResponseSchema])
def obtener_zonas():
    zona_entities = zona_service.obtener_todos_las_zonas()
    if zona_entities is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Zonas no encontradas"
        )
    return ZonaMapper.to_schema_list(zona_entities)


@router.get("/{id}", response_model = ZonaResponseSchema)
def obtener_aula_por_id(id: int):
    zona_entity = zona_service.obtener_zona_por_id(id)
    if zona_entity is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Zona no encontrada"
        )
    return ZonaMapper.to_schema(zona_entity)