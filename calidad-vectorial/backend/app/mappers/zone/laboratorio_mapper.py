from app.mappers.sector.zona_mapper import ZonaMapper
from app.models.zone.laboratorio import Laboratorio
from app.schemas.zone.laboratorio_response import LaboratorioResponseSchema


class LaboratorioMapper:
    @staticmethod
    def to_entity(schema: LaboratorioResponseSchema) -> Laboratorio:
        return Laboratorio(
            id=schema.id,
            nombre=schema.nombre,
            referencia=schema.referencia,
            descripcion=schema.descripcion,
            zona=ZonaMapper.to_entity(schema.zona),
        )

    @staticmethod
    def to_schema(entity: Laboratorio) -> LaboratorioResponseSchema:
        return LaboratorioResponseSchema(
            id=entity.id,
            nombre=entity.nombre,
            referencia=entity.referencia,
            descripcion=entity.descripcion,
        )

    @staticmethod
    def to_schema_list(entities: list[Laboratorio]) -> list[LaboratorioResponseSchema]:
        return [LaboratorioMapper.to_schema(entity) for entity in entities]
