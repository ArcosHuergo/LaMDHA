from app.mappers.sector.zona_mapper import ZonaMapper
from app.mappers.zone.zone_mapper_utils import ZoneMapperUtills
from app.models.zone.patio import Patio
from app.schemas.zone.patio_response import PatioResponseSchema


class PatioMapper:
    """Mapea entre entidades de patio y sus esquemas."""

    @staticmethod
    def to_entity(schema: PatioResponseSchema) -> Patio:
        """Convierte un esquema de patio en una entidad.

        Args:
            schema: Esquema de patio que se desea convertir.

        Returns:
            Entidad de patio creada a partir del esquema.
        """
        return Patio(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Patio) -> PatioResponseSchema:
        """Convierte una entidad de patio en un esquema de respuesta.

        Args:
            entity: Entidad de patio que se desea convertir.

        Returns:
            Esquema de respuesta creado a partir de la entidad.
        """
        data = ZoneMapperUtills.extraer_data_zone(entity.nombre)
        return PatioResponseSchema(
            id=entity.id,
            tipo=data["tipo"],
            referencia=entity.referencia,
            zona_color=data["zona_color"],
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(
        entities: list[Patio],
    ) -> list[PatioResponseSchema]:
        """Convierte una lista de entidades de patio en esquemas.

        Args:
            entities: Lista de entidades de patio.

        Returns:
            Lista de esquemas de respuesta de patio.
        """
        return [PatioMapper.to_schema(entity) for entity in entities]
