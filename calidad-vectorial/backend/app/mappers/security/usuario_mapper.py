from app.models.security.usuario import Usuario
from app.schemas.security.register import RegisterSchema
from app.schemas.security.usuario_response import UsuarioResponseSchema


class UsuarioMapper:
    """Mapea entre entidades de usuario y sus esquemas."""

    @staticmethod
    def to_entity(schema: RegisterSchema) -> Usuario:
        """Convierte un esquema de registro en una entidad de usuario.

        Args:
            schema: Esquema con los datos del usuario a registrar.

        Returns:
            Entidad de usuario creada a partir del esquema.
        """
        return Usuario(username=schema.username, nickname=schema.username)

    @staticmethod
    def to_schema(entity: Usuario) -> UsuarioResponseSchema:
        """Convierte una entidad de usuario en un esquema de respuesta.

        Args:
            entity: Entidad de usuario que se desea convertir.

        Returns:
            Esquema de respuesta con los datos públicos del usuario.
        """
        return UsuarioResponseSchema(
            username=entity.username,
            nickname=entity.nickname,
        )

    @staticmethod
    def to_schema_list(
        entites: list[Usuario],
    ) -> list[UsuarioResponseSchema]:
        """Convierte una lista de entidades de usuario en esquemas.

        Args:
            entites: Lista de entidades de usuario.

        Returns:
            Lista de esquemas de respuesta de usuario.
        """
        return [UsuarioMapper.to_schema(entity) for entity in entites]
