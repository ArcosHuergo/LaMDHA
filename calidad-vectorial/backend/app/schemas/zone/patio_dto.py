from pydantic import BaseModel

class PatioDTO(BaseModel):
    nombre: str
    referencia: str
    descripcion: str

    