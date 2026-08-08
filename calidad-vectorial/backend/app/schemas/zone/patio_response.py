from pydantic import BaseModel

class PatioResponseSchema(BaseModel):
    nombre: str
    referencia: str
    descripcion: str