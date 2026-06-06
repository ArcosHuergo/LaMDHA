from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.pasillo_service import PasilloService


router = APIRouter()
service = PasilloService()

@router.get("/pasillo/", tags=["Pasillo"])
def obtener_pasillos():
    return service.obtener_todos_los_pasillos()

@router.get("/pasillo/{id}", tags=["Pasillo"])
def obtener_pasillo_por_id(id: int):
    return service.obtener_pasillo_por_id(id)

