from pydantic import BaseModel


class ClassPrediction(BaseModel):
    """Una clase individual devuelta por el modelo, con su confianza."""

    clase: str
    confianza: float


class RoboflowPrediction(BaseModel):
    predicciones: list[ClassPrediction]
    model_id: str | None = None
    inference_id: str | None = None
