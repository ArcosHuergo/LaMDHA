from app.models.sector.zona import Zona
from app.schemas.sector.zona_response import ZonaResponseSchema


class ZonaMapper:
    """Mapea entre entidades de zona y sus esquemas."""

    @staticmethod
    def to_entity(schema: ZonaResponseSchema) -> Zona:
        """Convierte un esquema de zona en una entidad.

        Args:
            schema: Esquema de zona que se desea convertir.

        Returns:
            Entidad de zona creada a partir del esquema.
        """
        return Zona(id=schema.id, color=schema.color)

    @staticmethod
    def to_schema(entity: Zona) -> ZonaResponseSchema:
        """Convierte una entidad de zona en un esquema.

        Args:
            entity: Entidad de zona que se desea convertir.

        Returns:
            Esquema de zona creado a partir de la entidad.
        """
        return ZonaResponseSchema(id=entity.id, color=entity.color)

    @staticmethod
    def to_schema_list(entities: list[Zona]) -> list[ZonaResponseSchema]:
        """Convierte una lista de entidades de zona en esquemas.

        Args:
            entities: Lista de entidades de zona.

        Returns:
            Lista de esquemas de zona.
        """
        return [ZonaMapper.to_schema(entity) for entity in entities]
