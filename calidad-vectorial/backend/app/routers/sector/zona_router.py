from app.mappers.sector.zona_mapper import ZonaMapper
from app.schemas.sector.zona_response import ZonaResponseSchema
from app.services.log.foto_storage_service import (
    FotoNoEncontradaError,
    FotoStorageError,
    descargar_foto_referencia,
)
from app.services.sector.zona_service import ZonaService
from fastapi import APIRouter, HTTPException, Response, status

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


@router.get("/referencia/{nombre}")
def obtener_foto_referencia_por_nombre(nombre: str):
    """Obtiene la foto de referencia de un sector por su nombre.

    Args:

        nombre: Nombre del sector.

    Returns:

        Respuesta HTTP con el archivo de imagen de referencia del sector.

    Raises:

        HTTPException: Si no existe una foto de referencia para el sector o si
            no pudo recuperarse del almacenamiento.
    """
    try:
        contenido = descargar_foto_referencia(nombre)
    except FotoNoEncontradaError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró la imagen de referencia del sector.",
        )
    except FotoStorageError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="No se pudo recuperar la imagen de referencia del sector.",
        )
    return Response(content=contenido, media_type="image/jpeg")