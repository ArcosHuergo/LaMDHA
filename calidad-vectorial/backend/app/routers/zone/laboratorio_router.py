from app.mappers.zone.laboratorio_mapper import LaboratorioMapper
from app.schemas.zone.laboratorio_response import LaboratorioResponseSchema
from app.services.zone.laboratorio_service import LaboratorioService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/laboratorio", tags=["Laboratorio"])
laboratorio_service = LaboratorioService()


@router.get("", response_model=list[LaboratorioResponseSchema])
def obtener_laboratorios():
    """Obtiene todos los laboratorios.

    Returns:

        Lista de laboratorios convertidos a su esquema de respuesta.

    Raises:

        HTTPException: Si no se encuentran laboratorios.
    """
    laboratorio_entities = laboratorio_service.obtener_todos_los_laboratorios()
    if laboratorio_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorios no encontrados"
        )
    return LaboratorioMapper.to_schema_list(laboratorio_entities)


@router.get("/{id}", response_model=LaboratorioResponseSchema)
def obtener_laboratorio_por_id(id: int):
    """Obtiene un laboratorio por su identificador.

    Args:

        id: Identificador del laboratorio.

    Returns:

        Laboratorio convertido a su esquema de respuesta.

    Raises:

        HTTPException: Si no se encuentra el laboratorio.
    """
    laboratorio_entity = laboratorio_service.obtener_laboratorio_por_id(id)
    if laboratorio_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorio no encontrado"
        )
    return LaboratorioMapper.to_schema(laboratorio_entity)


@router.get("/nombre/{nombre}", response_model=LaboratorioResponseSchema)
def obtener_laboratorio_por_nombre(nombre: str):
    """Obtiene un laboratorio por su nombre.

    Args:

        nombre: Nombre del laboratorio.

    Returns:

        Laboratorio convertido a su esquema de respuesta.

    Raises:
    
        HTTPException: Si no se encuentra el laboratorio.
    """
    laboratorio_entity = laboratorio_service.obtener_laboratorio_por_nombre(nombre)
    if laboratorio_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorio no encontrado"
        )
    return LaboratorioMapper.to_schema(laboratorio_entity)
