from app.mappers.sector.zona_mapper import ZonaMapper
from app.mappers.zone.zone_mapper_utils import ZoneMapperUtills
from app.models.zone.biblioteca import Biblioteca
from app.schemas.zone.biblioteca_response import BibliotecaResponseSchema


class BibliotecaMapper:
    """Mapea entre entidades de biblioteca y sus esquemas."""

    @staticmethod
    def to_entity(schema: BibliotecaResponseSchema) -> Biblioteca:
        """Convierte un esquema de biblioteca en una entidad.

        Args:
            schema: Esquema de biblioteca que se desea convertir.

        Returns:
            Entidad de biblioteca creada a partir del esquema.
        """
        return Biblioteca(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Biblioteca) -> BibliotecaResponseSchema:
        """Convierte una entidad de biblioteca en un esquema de respuesta.

        Args:
            entity: Entidad de biblioteca que se desea convertir.

        Returns:
            Esquema de respuesta creado a partir de la entidad.
        """
        data = ZoneMapperUtills.extraer_data_zone(entity.nombre)
        return BibliotecaResponseSchema(
            id=entity.id,
            tipo=data["tipo"],
            referencia=entity.referencia,
            zona_color=data["zona_color"],
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(
        entities: list[Biblioteca],
    ) -> list[BibliotecaResponseSchema]:
        """Convierte una lista de entidades de biblioteca en esquemas.

        Args:
            entities: Lista de entidades de biblioteca.

        Returns:
            Lista de esquemas de respuesta de biblioteca.
        """
        return [BibliotecaMapper.to_schema(entity) for entity in entities]
