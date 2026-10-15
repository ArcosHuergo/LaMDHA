from pydantic import BaseModel


class BibliotecaResponseSchema(BaseModel):
    id: int
    tipo: str
    referencia: str
    zona_color: str
    descripcion: str
