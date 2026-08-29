from app.models.zone.pasillo import Pasillo
from app.schemas.zone.pasillo_response import PasilloResponseSchema
from app.mappers.sector.zona_mapper import ZonaMapper

class PasilloMapper:

    @staticmethod
    def to_entity(schema: PasilloResponseSchema) -> Pasillo:
        return Pasillo(
            id=schema.id, 
            nombre=schema.nombre, 
            descripcion=schema.descripcion, 
            zona=ZonaMapper.to_entity(schema.zona)) 

    @staticmethod
    def to_schema(entity: Pasillo) -> PasilloResponseSchema:
        return PasilloResponseSchema(
            id=entity.id, 
            nombre=entity.nombre, 
            descripcion=entity.descripcion)

    @staticmethod
    def to_schema_list(entities: list[Pasillo]) -> list[PasilloResponseSchema]:
        return [PasilloMapper.to_schema(entity) for entity in entities]