from app.mappers.sector.zona_mapper import ZonaMapper
from app.mappers.zone.zone_mapper_utils import ZoneMapperUtills
from app.models.zone.aula import Aula
from app.schemas.zone.aula_response import AulaResponseSchema


class AulaMapper:
    """Mapea entre entidades de aula y sus esquemas."""

    @staticmethod
    def to_entity(schema: AulaResponseSchema) -> Aula:
        """Convierte un esquema de aula en una entidad.

        Args:
            schema: Esquema de aula que se desea convertir.

        Returns:
            Entidad de aula creada a partir del esquema.
        """
        return Aula(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Aula) -> AulaResponseSchema:
        """Convierte una entidad de aula en un esquema de respuesta.

        Args:
            entity: Entidad de aula que se desea convertir.

        Returns:
            Esquema de respuesta creado a partir de la entidad.
        """
        data = ZoneMapperUtills.extraer_data_zone(entity.nombre)
        return AulaResponseSchema(
            id=entity.id,
            tipo=data["tipo"],
            referencia=entity.referencia,
            zona_color=data["zona_color"],
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(entities: list[Aula]) -> list[AulaResponseSchema]:
        """Convierte una lista de entidades de aula en esquemas.

        Args:
            entities: Lista de entidades de aula.

        Returns:
            Lista de esquemas de respuesta de aula.
        """
        return [AulaMapper.to_schema(entity) for entity in entities]
