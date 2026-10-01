from app.mappers.sector.zona_mapper import ZonaMapper
from app.models.zone.pasillo import Pasillo
from app.schemas.zone.pasillo_response import PasilloResponseSchema


class PasilloMapper:
    """Mapea entre entidades de pasillo y sus esquemas."""

    @staticmethod
    def to_entity(schema: PasilloResponseSchema) -> Pasillo:
        """Convierte un esquema de pasillo en una entidad.

        Args:
            schema: Esquema de pasillo que se desea convertir.

        Returns:
            Entidad de pasillo creada a partir del esquema.
        """
        return Pasillo(
            id=schema.id,
            nombre=schema.nombre,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Pasillo) -> PasilloResponseSchema:
        """Convierte una entidad de pasillo en un esquema de respuesta.

        Args:
            entity: Entidad de pasillo que se desea convertir.

        Returns:
            Esquema de respuesta creado a partir de la entidad.
        """
        return PasilloResponseSchema(
            id=entity.id,
            nombre=entity.nombre,
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(
        entities: list[Pasillo],
    ) -> list[PasilloResponseSchema]:
        """Convierte una lista de entidades de pasillo en esquemas.

        Args:
            entities: Lista de entidades de pasillo.

        Returns:
            Lista de esquemas de respuesta de pasillo.
        """
        return [PasilloMapper.to_schema(entity) for entity in entities]
