from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.biblioteca_service import BibliotecaService
from app.mappers.zone.biblioteca_mapper import BibliotecaMapper

router = APIRouter()
biblioteca_service = BibliotecaService()

@router.get("/biblioteca/", tags=["Biblioteca"])
def obtener_bibliotecas():
    return BibliotecaMapper.to_schema_list(biblioteca_service.obtener_todas_las_bibliotecas())

@router.get("/biblioteca/{id}", tags=["Biblioteca"])
def obtener_biblioteca_por_id(id: int):
    return BibliotecaMapper.to_schema(biblioteca_service.obtener_biblioteca_por_id(id))