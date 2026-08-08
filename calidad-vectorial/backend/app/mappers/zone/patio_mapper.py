from app.models.zone.patio import Patio
from app.schemas.zone.patio_response import PatioResponseSchema
from app.mappers.sector.zona_mapper import ZonaMapper

class PatioMapper:

    # nico wachin cambia despues  PatioRequestaSchema
    @staticmethod
    def to_entity(schema: PatioResponseSchema) -> Patio:
        return Patio(id=schema.id, nombre=schema.nombre, referencia=schema.referencia, descripcion=schema.descripcion, zona=ZonaMapper.to_entity(schema.zona)) 

    @staticmethod
    def to_schema(entity: Patio) -> Patio:
        return PatioResponseSchema(id=entity.id, nombre=entity.nombre, referencia=entity.referencia, descripcion=entity.descripcion, zona_id=entity.zona_id, zona=entity.zona)

