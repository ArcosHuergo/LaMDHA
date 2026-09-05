from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.biblioteca_service import BibliotecaService
from app.mappers.zone.biblioteca_mapper import BibliotecaMapper
from app.schemas.zone.biblioteca_response import BibliotecaResponseSchema

router = APIRouter(prefix = "/biblioteca", tags=["Biblioteca"])
biblioteca_service = BibliotecaService()

@router.get("", response_model = list[BibliotecaResponseSchema])
def obtener_bibliotecas():
    return BibliotecaMapper.to_schema_list(biblioteca_service.obtener_todas_las_bibliotecas())

@router.get("/{id}", response_model = BibliotecaResponseSchema)
def obtener_biblioteca_por_id(id: int):
    return BibliotecaMapper.to_schema(biblioteca_service.obtener_biblioteca_por_id(id))