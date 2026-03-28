from fastapi import APIRouter

router = APIRouter()

@router.get("/usuario")
def prueba():
    return "hola"