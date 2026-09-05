from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.pasillo_service import PasilloService
from app.mappers.zone.pasillo_mapper import PasilloMapper
from app.schemas.zone.pasillo_response import PasilloResponseSchema

router = APIRouter(prefix = "/pasillo", tags=["Pasillo"])
pasillo_service = PasilloService()

@router.get("", response_model = list[PasilloResponseSchema])
def obtener_pasillos():
    return PasilloMapper.to_schema_list(pasillo_service.obtener_todos_los_pasillos())

@router.get("/{id}", response_model = PasilloResponseSchema)
def obtener_pasillo_por_id(id: int):
    return PasilloMapper.to_schema(pasillo_service.obtener_pasillo_por_id(id))

