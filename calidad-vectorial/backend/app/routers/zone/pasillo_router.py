from fastapi import APIRouter, HTTPException, status

from app.services.zone.pasillo_service import PasilloService
from app.mappers.zone.pasillo_mapper import PasilloMapper
from app.schemas.zone.pasillo_response import PasilloResponseSchema

router = APIRouter(prefix = "/pasillo", tags=["Pasillo"])
pasillo_service = PasilloService()

@router.get("", response_model = list[PasilloResponseSchema])
def obtener_pasillos():
    pasillo_entities = pasillo_service.obtener_todos_los_pasillos()
    if pasillo_entities is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Pasillos no encontrados"
        )
    return PasilloMapper.to_schema_list(pasillo_entities)


@router.get("/{id}", response_model = PasilloResponseSchema)
def obtener_pasillo_por_id(id: int):
    pasillo_entity = pasillo_service.obtener_pasillo_por_id(id)
    if pasillo_entity is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Pasillo no encontrado"
        )
    return PasilloMapper.to_schema(pasillo_entity)


@router.get("/nombre/{nombre}", response_model = PasilloResponseSchema)
def obtener_pasillo_por_nombre(nombre: str):
    pasillo_entity = pasillo_service.obtener_pasillo_por_nombre(nombre)
    if pasillo_entity is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Pasillo no encontrado"
        )
    return PasilloMapper.to_schema(pasillo_entity)