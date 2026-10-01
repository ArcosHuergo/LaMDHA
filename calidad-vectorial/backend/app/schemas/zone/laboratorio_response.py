from pydantic import BaseModel


class LaboratorioResponseSchema(BaseModel):
    id: int
    nombre: str
    referencia: str
    descripcion: str
