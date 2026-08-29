from app.models.zone.patio import Patio
from app.schemas.zone.patio_response import PatioResponseSchema
from app.mappers.sector.zona_mapper import ZonaMapper

class PatioMapper:

    @staticmethod
    def to_entity(schema: PatioResponseSchema) -> Patio:
        return Patio(
            id=schema.id, 
            nombre=schema.nombre, 
            referencia=schema.referencia,
            descripcion=schema.descripcion, 
            zona=ZonaMapper.to_entity(schema.zona)) 

    @staticmethod
    def to_schema(entity: Patio) -> PatioResponseSchema:
        return PatioResponseSchema(
            id=entity.id, 
            nombre=entity.nombre, 
            referencia=entity.referencia, 
            descripcion=entity.descripcion)

    @staticmethod
    def to_schema_list(entities: list[Patio]) -> list[PatioResponseSchema]:
        return [PatioMapper.to_schema(entity) for entity in entities]

