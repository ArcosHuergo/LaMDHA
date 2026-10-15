from pydantic import BaseModel


class PasilloResponseSchema(BaseModel):
    id: int
    tipo: str
    zona_color: str
    descripcion: str
