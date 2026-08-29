from pydantic import BaseModel

class BibliotecaResponseSchema(BaseModel):
    id: int
    nombre: str
    referencia: str
    descripcion: str