from pydantic import BaseModel


class ClassPrediction(BaseModel):
    """Una clase individual devuelta por el modelo, con su confianza."""

    clase: str
    confianza: float


class RoboflowPrediction(BaseModel):
    """
    Resultado ya parseado del workflow "lamdha" (clasificación de ubicación
    dentro del edificio: aula/pasillo/patio/laboratorio, ej. "Pasillo-PB-Azul").

    "predicciones" trae TODAS las clases que superaron el umbral de
    confianza —incluida la ganadora— en una única lista, ordenada de mayor a
    menor confianza. La clase ganadora es simplemente `predicciones[0]`; no
    hay campos separados para "la ganadora" vs. "las alternativas" porque el
    front-end las trata a todas por igual (ej. para renderizarlas como lista).
    """

    predicciones: list[ClassPrediction]
    model_id: str | None = None
    inference_id: str | None = None
