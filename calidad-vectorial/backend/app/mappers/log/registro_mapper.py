from app.models.log.registro import Registro
from app.schemas.log.registro_feedback import RegistroFeedbackSchema

class RegistroMapper:

    @staticmethod
    def to_schema(entity: Registro) -> RegistroFeedbackSchema:
        return RegistroFeedbackSchema(id=entity.id, prediccion_correcta=entity.prediccion_correcta)