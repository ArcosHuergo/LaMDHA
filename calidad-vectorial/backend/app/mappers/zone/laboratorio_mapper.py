from app.models.zone.laboratorio import Laboratorio
from app.schemas.zone.laboratorio_response import LaboratorioRespuestaSchema
from app.mappers.sector.zona_mapper import ZonaMapper

class LaboratorioMapper:

    @staticmethod
    def to_entity(schema: LaboratorioRespuestaSchema) -> Laboratorio:
        return Laboratorio(id=schema.id, nombre=schema.nombre, referencia=schema.referencia, descripcion=schema.descripcion, zona=ZonaMapper.to_entity(schema.zona)) 

    @staticmethod
    def to_schema(entity: Laboratorio) -> LaboratorioRespuestaSchema:
        return LaboratorioRespuestaSchema(id=entity.id, nombre=entity.nombre, referencia=entity.referencia, descripcion=entity.descripcion, zona_id=entity.zona_id, zona=entity.zona)