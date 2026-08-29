from app.models.zone.aula import Aula
from app.schemas.zone.aula_response import AulaResponseSchema
from app.mappers.sector.zona_mapper import ZonaMapper

class AulaMapper:

    # nico wachin cambia despues AulaRequestaSchema (?)
    @staticmethod
    def to_entity(schema: AulaResponseSchema) -> Aula:
        return Aula(id=schema.id, nombre=schema.nombre, referencia=schema.referencia, descripcion=schema.descripcion, zona=ZonaMapper.to_entity(schema.zona)) 

    @staticmethod
    def to_schema(entity: Aula) -> AulaResponseSchema:
        return AulaResponseSchema(id=entity.id, nombre=entity.nombre, referencia=entity.referencia, descripcion=entity.descripcion, zona_id=entity.zona_id, zona=entity.zona)