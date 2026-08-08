from pydantic import BaseModel

class PasilloResponseSchema(BaseModel):
    id: int
    nombre: str
    descripcion: str
    