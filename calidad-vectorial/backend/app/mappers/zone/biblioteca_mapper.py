from app.mappers.sector.zona_mapper import ZonaMapper
from app.models.zone.biblioteca import Biblioteca
from app.schemas.zone.biblioteca_response import BibliotecaResponseSchema


class BibliotecaMapper:
    @staticmethod
    def to_entity(schema: BibliotecaResponseSchema) -> Biblioteca:
        return Biblioteca(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Biblioteca) -> BibliotecaResponseSchema:
        return BibliotecaResponseSchema(
            id=entity.id,
            nombre=entity.nombre,
            referencia=entity.referencia,
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(entities: list[Biblioteca]) -> list[BibliotecaResponseSchema]:
        return [BibliotecaMapper.to_schema(entity) for entity in entities]
