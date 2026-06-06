from pydantic import BaseModel

class AulaDTO(BaseModel):
    nombre: str
    referencia: str
    descripcion: str