from app.mappers.sector.zona_mapper import ZonaMapper
from app.models.zone.laboratorio import Laboratorio
from app.schemas.zone.laboratorio_response import LaboratorioResponseSchema


class LaboratorioMapper:
    """Mapea entre entidades de laboratorio y sus esquemas."""

    @staticmethod
    def to_entity(schema: LaboratorioResponseSchema) -> Laboratorio:
        """Convierte un esquema de laboratorio en una entidad.

        Args:
            schema: Esquema de laboratorio que se desea convertir.

        Returns:
            Entidad de laboratorio creada a partir del esquema.
        """
        return Laboratorio(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Laboratorio) -> LaboratorioResponseSchema:
        """Convierte una entidad de laboratorio en un esquema de respuesta.

        Args:
            entity: Entidad de laboratorio que se desea convertir.

        Returns:
            Esquema de respuesta creado a partir de la entidad.
        """
        return LaboratorioResponseSchema(
            id=entity.id,
            nombre=entity.nombre,
            referencia=entity.referencia,
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(
        entities: list[Laboratorio],
    ) -> list[LaboratorioResponseSchema]:
        """Convierte una lista de entidades de laboratorio en esquemas.

        Args:
            entities: Lista de entidades de laboratorio.

        Returns:
            Lista de esquemas de respuesta de laboratorio.
        """
        return [LaboratorioMapper.to_schema(entity) for entity in entities]
