from app.models.log.registro import Registro
from app.schemas.log.registro_completo import RegistroCompletoSchema
from app.schemas.log.registro_feedback import RegistroFeedbackSchema


class RegistroMapper:
    @staticmethod
    def to_schema(entity: Registro) -> RegistroFeedbackSchema:
        return RegistroFeedbackSchema(prediccion_correcta=entity.prediccion_correcta)

    @staticmethod
    def to_schema_completo(entity: Registro) -> RegistroCompletoSchema:
        return RegistroCompletoSchema(
            id=entity.id,
            prediccion_correcta=entity.prediccion_correcta,
            url_foto=f"/registro/{entity.id}/foto" if entity.url_foto else None,
            fecha_creacion=entity.fecha_creacion,
        )

    @staticmethod
    def to_schema_completo_list(
        entities: list[Registro],
    ) -> list[RegistroCompletoSchema]:
        return [RegistroMapper.to_schema_completo(entity) for entity in entities]
