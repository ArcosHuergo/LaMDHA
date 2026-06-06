from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.zone.aula_service import AulaService

router = APIRouter()
service = AulaService()

@router.get("/aula/", tags=["Aula"])
def obtener_aulas():
    return service.obtener_todos_las_aulas()

@router.get("/aula/{id}", tags=["Aula"])
def obtener_aula_por_id(id: int):
    return service.obtener_aula_por_id(id)

