from pydantic import BaseModel


class PatioResponseSchema(BaseModel):
    id: int
    tipo: str
    referencia: str
    zona_color: str
    descripcion: str
