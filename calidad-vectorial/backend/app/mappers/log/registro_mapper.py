from app.models.log.registro import Registro
from app.schemas.log.registro_completo import RegistroCompletoSchema
from app.schemas.log.registro_feedback import RegistroFeedbackSchema


class RegistroMapper:
    """Mapea entidades de registro a sus esquemas de respuesta."""

    @staticmethod
    def to_schema(entity: Registro) -> RegistroFeedbackSchema:
        """Convierte un registro en un esquema de feedback.

        Args:
            entity: Entidad de registro que se desea convertir.

        Returns:
            Esquema de feedback con el resultado de la predicción.
        """
        return RegistroFeedbackSchema(prediccion_correcta=entity.prediccion_correcta)

    @staticmethod
    def to_schema_completo(entity: Registro) -> RegistroCompletoSchema:
        """Convierte un registro en un esquema con información completa.

        Args:
            entity: Entidad de registro que se desea convertir.

        Returns:
            Esquema con la información completa del registro.
        """
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
        """Convierte una lista de registros en esquemas completos.

        Args:
            entities: Lista de entidades de registro.

        Returns:
            Lista de esquemas con la información completa de cada registro.
        """
        return [RegistroMapper.to_schema_completo(entity) for entity in entities]
