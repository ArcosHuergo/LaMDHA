from datetime import datetime

from pydantic import BaseModel


class RegistroCompletoSchema(BaseModel):
    id: int
    prediccion_correcta: bool | None
    fecha_creacion: datetime
    sector: str | None
    piso: str | None
    tipo: str | None
    referencia: str | None
    confianza: float | None
