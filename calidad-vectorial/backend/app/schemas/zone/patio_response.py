from pydantic import BaseModel

class PatioResponseSchema(BaseModel):
    id: int
    nombre: str
    referencia: str
    descripcion: str