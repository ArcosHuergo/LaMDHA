from app.models.sector.zona import Zona
from app.schemas.sector.zona_response import ZonaResponseSchema


class ZonaMapper:
    @staticmethod
    def to_entity(schema: ZonaResponseSchema) -> Zona:
        return Zona(id=schema.id, color=schema.color)

    @staticmethod
    def to_schema(entity: Zona) -> Zona:
        return ZonaResponseSchema(id=entity.id, color=entity.color)

    @staticmethod
    def to_schema_list(entities: list[Zona]) -> list[ZonaResponseSchema]:
        return [ZonaMapper.to_schema(entity) for entity in entities]
