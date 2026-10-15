from pydantic import BaseModel


class AulaResponseSchema(BaseModel):
    id: int
    tipo: str
    referencia: str
    zona_color: str
    descripcion: str
