from pydantic import BaseModel


class LaboratorioResponseSchema(BaseModel):
    id: int
    tipo: str
    referencia: str
    zona_color: str
    descripcion: str
