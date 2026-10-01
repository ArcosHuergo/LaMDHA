from app.mappers.zone.aula_mapper import AulaMapper
from app.schemas.zone.aula_response import AulaResponseSchema
from app.services.zone.aula_service import AulaService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/aula", tags=["Aula"])
aula_service = AulaService()


@router.get("", response_model=list[AulaResponseSchema])
def obtener_aulas():
    """Obtiene todas las aulas.

    Returns:
        Lista de aulas convertidas a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentran aulas.
    """
    aula_entities = aula_service.obtener_todas_las_aulas()
    if aula_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aulas no encontradas"
        )
    return AulaMapper.to_schema_list(aula_entities)


@router.get("/{id}", response_model=AulaResponseSchema)
def obtener_aula_por_id(id: int):
    """Obtiene un aula por su identificador.

    Args:
        id: Identificador del aula.

    Returns:
        Aula convertida a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentra el aula.
    """
    aula_entity = aula_service.obtener_aula_por_id(id)
    if aula_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aula no encontrada"
        )
    return AulaMapper.to_schema(aula_entity)


@router.get("/nombre/{nombre}", response_model=AulaResponseSchema)
def obtener_aula_por_nombre(nombre: str):
    """Obtiene un aula por su nombre.

    Args:
        nombre: Nombre del aula.

    Returns:
        Aula convertida a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentra el aula.
    """
    aula_entity = aula_service.obtener_aula_por_nombre(nombre)
    if aula_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aula no encontrada"
        )
    return AulaMapper.to_schema(aula_entity)
