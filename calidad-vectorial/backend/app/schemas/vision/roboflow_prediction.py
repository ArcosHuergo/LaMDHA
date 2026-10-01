from pydantic import BaseModel, computed_field


class ClassPrediction(BaseModel):
    """Una clase individual devuelta por el modelo, con su confianza."""

    clase: str
    confianza: float


class RoboflowPrediction(BaseModel):
    predicciones: list[ClassPrediction]
    model_id: str | None = None
    inference_id: str | None = None
    registro_id: int | None = None

    @computed_field
    @property
    def piso(self) -> int | None:
        if not self.predicciones:
            return None
        ganadora = max(self.predicciones, key=lambda p: p.confianza)
        partes = ganadora.clase.split("-")
        if len(partes) < 2:
            return None
        return partes[1]
