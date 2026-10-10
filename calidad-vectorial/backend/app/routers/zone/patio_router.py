from app.mappers.zone.patio_mapper import PatioMapper
from app.schemas.zone.patio_response import PatioResponseSchema
from app.services.zone.patio_service import PatioService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/patio", tags=["Patio"])
patio_service = PatioService()


@router.get("", response_model=list[PatioResponseSchema])
def obtener_patios():
    """Obtiene todos los patios.
    
        Returns:
    
            Lista de patios convertidos a su esquema de respuesta.
    
        Raises:
    
            HTTPException: Si no se encuentran patios.
        """
    patio_entities = patio_service.obtener_todos_los_patios()
    if patio_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patios no encontrados"
        )
    return PatioMapper.to_schema_list(patio_entities)


@router.get("/{id}", response_model=PatioResponseSchema)
def obtener_patio_por_id(id: int):
    """Obtiene un patio por su identificador.
    
        Args:
    
            id: Identificador del patio.
    
        Returns:
    
            Patio convertido a su esquema de respuesta.
    
        Raises:
    
            HTTPException: Si no se encuentra el patio.
        """
    patio_entity = patio_service.obtener_patio_por_id(id)
    if patio_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patio no encontrado"
        )
    return PatioMapper.to_schema(patio_entity)


@router.get("/nombre/{nombre}", response_model=PatioResponseSchema)
def obtener_patio_por_nombre(nombre: str):
    """Obtiene un patio por su nombre.
    
        Args:
    
            nombre: Nombre del patio.
    
        Returns:
    
            Patio convertido a su esquema de respuesta.
    
        Raises:
        
            HTTPException: Si no se encuentra el patio.
        """
    patio_entity = patio_service.obtener_patio_por_nombre(nombre)
    if patio_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patio no encontrado"
        )
    return PatioMapper.to_schema(patio_entity)
