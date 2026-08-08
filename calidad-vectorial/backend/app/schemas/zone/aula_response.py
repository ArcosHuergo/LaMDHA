from pydantic import BaseModel

class AulaResponseSchema(BaseModel):
    nombre: str
    referencia: str
    descripcion: str

