from pydantic import BaseModel

class PasilloDTO(BaseModel):
    nombre: str
    descripcion: str
    