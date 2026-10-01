from app.mappers.sector.zona_mapper import ZonaMapper
from app.schemas.sector.zona_response import ZonaResponseSchema
from app.services.sector.zona_service import ZonaService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/zona", tags=["Zona"])
zona_service = ZonaService()


@router.get("", response_model=list[ZonaResponseSchema])
def obtener_zonas():
    """Obtiene todas las zonas.

    Returns:
        Lista de zonas convertidas a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentran zonas.
    """
    zona_entities = zona_service.obtener_todos_las_zonas()
    if zona_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Zonas no encontradas"
        )
    return ZonaMapper.to_schema_list(zona_entities)


@router.get("/{id}", response_model=ZonaResponseSchema)
def obtener_aula_por_id(id: int):
    """Obtiene una zona por su identificador.

    Args:
        id: Identificador de la zona.

    Returns:
        Zona convertida a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentra la zona.
    """
    zona_entity = zona_service.obtener_zona_por_id(id)
    if zona_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Zona no encontrada"
        )
    return ZonaMapper.to_schema(zona_entity)