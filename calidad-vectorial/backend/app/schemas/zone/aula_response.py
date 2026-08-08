from pydantic import BaseModel

class AulaResponseSchema(BaseModel):
    id: int
    nombre: str
    referencia: str
    descripcion: str

