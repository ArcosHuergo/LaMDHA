from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.patio_service import PatioService

router = APIRouter()
service = PatioService()

@router.get("/patio/", tags=["Patio"])
def obtener_patios():
    return service.obtener_todos_los_patios()

@router.get("/patio/{id}", tags=["Patio"])
def obtener_patio_por_id(id: int):
    return service.obtener_patio_por_id(id)