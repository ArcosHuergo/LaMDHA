from app.models.security.usuario import Usuario
from app.schemas.security.register import RegisterSchema
from app.schemas.security.usuario_response import UsuarioResponseSchema

class UsuarioMapper:

    @staticmethod
    def to_entity(schema: RegisterSchema) -> Usuario:
        return Usuario(username=schema.username, nickname=schema.username)

    @staticmethod
    def to_schema(entity: Usuario) -> UsuarioResponseSchema:
        return UsuarioResponseSchema(username=entity.username, nickname=entity.nickname)

    @staticmethod
    def to_schema_list(entites: list[Usuario] ) -> list[UsuarioResponseSchema]:
        return [UsuarioMapper.to_schema(entity) for entity in entites]
