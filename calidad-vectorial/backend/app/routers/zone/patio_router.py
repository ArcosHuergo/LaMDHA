from fastapi import APIRouter, HTTPException, status

from app.services.zone.patio_service import PatioService
from app.mappers.zone.patio_mapper import PatioMapper
from app.schemas.zone.patio_response import PatioResponseSchema

router = APIRouter(prefix = "/patio", tags=["Patio"])
patio_service = PatioService()

@router.get("", response_model = list[PatioResponseSchema])
def obtener_patios():
    patio_entities = patio_service.obtener_todos_los_patios()
    if patio_entities is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Patios no encontrados"
        )
    return PatioMapper.to_schema_list(patio_entities)


@router.get("/{id}", response_model = PatioResponseSchema)
def obtener_patio_por_id(id: int):
    patio_entity = patio_service.obtener_patio_por_id(id)
    if patio_entity is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Patio no encontrado"
        )
    return PatioMapper.to_schema(patio_entity)


@router.get("/nombre/{nombre}", response_model = PatioResponseSchema)
def obtener_patio_por_nombre(nombre: str):
    patio_entity = patio_service.obtener_patio_por_nombre(nombre)
    if patio_entity is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Patio no encontrado"
        )
    return PatioMapper.to_schema(patio_entity)
