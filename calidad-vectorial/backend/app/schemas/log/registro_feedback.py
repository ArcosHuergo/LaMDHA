from pydantic import BaseModel

class RegistroFeedbackSchema(BaseModel):
    prediccion_correcta: bool | None