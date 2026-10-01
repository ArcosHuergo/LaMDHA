from datetime import datetime

from pydantic import BaseModel


class RegistroCompletoSchema(BaseModel):
    id: int
    prediccion_correcta: bool | None
    url_foto: str | None
    fecha_creacion: datetime
