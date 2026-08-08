from pydantic import BaseModel

class PasilloResponseSchema(BaseModel):
    nombre: str
    descripcion: str
    