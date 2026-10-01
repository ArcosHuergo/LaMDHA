from app.mappers.zone.biblioteca_mapper import BibliotecaMapper
from app.schemas.zone.biblioteca_response import BibliotecaResponseSchema
from app.services.zone.biblioteca_service import BibliotecaService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/biblioteca", tags=["Biblioteca"])
biblioteca_service = BibliotecaService()


@router.get("", response_model=list[BibliotecaResponseSchema])
def obtener_bibliotecas():
    """Obtiene todas las bibliotecas.

    Returns:
        Lista de bibliotecas convertidas a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentran bibliotecas.
    """
    biblioteca_entities = biblioteca_service.obtener_todas_las_bibliotecas()
    if biblioteca_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bibliotecas no encontradas"
        )
    return BibliotecaMapper.to_schema_list(biblioteca_entities)


@router.get("/{id}", response_model=BibliotecaResponseSchema)
def obtener_biblioteca_por_id(id: int):
    """Obtiene una biblioteca por su identificador.

    Args:
        id: Identificador de la biblioteca.

    Returns:
        Biblioteca convertida a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentra la biblioteca.
    """
    biblioteca_entity = biblioteca_service.obtener_biblioteca_por_id(id)
    if biblioteca_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Biblioteca no encontrada"
        )
    return BibliotecaMapper.to_schema(biblioteca_entity)


@router.get("/nombre/{nombre}", response_model=BibliotecaResponseSchema)
def obtener_biblioteca_por_nombre(nombre: str):
    """Obtiene una biblioteca por su nombre.

    Args:
        nombre: Nombre de la biblioteca.

    Returns:
        Biblioteca convertida a su esquema de respuesta.

    Raises:
        HTTPException: Si no se encuentra la biblioteca.
    """
    biblioteca_entity = biblioteca_service.obtener_biblioteca_por_nombre(nombre)
    if biblioteca_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Biblioteca no encontrada"
        )
    return BibliotecaMapper.to_schema(biblioteca_entity)
