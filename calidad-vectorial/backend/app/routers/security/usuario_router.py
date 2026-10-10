from app.mappers.security.usuario_mapper import UsuarioMapper
from app.schemas.security.usuario_response import UsuarioResponseSchema
from app.services.security.usuario_service import UsuarioService
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/usuario", tags=["Usuario"])
usuario_service = UsuarioService()


@router.get("", response_model=list[UsuarioResponseSchema])
def obtener_usuarios():
    """Obtiene todos los usuarios.

    Returns:

        Lista de usuarios convertidos a su esquema de respuesta.

    Raises:
    
        HTTPException: Si no se encuentran usuarios.
    """
    usuario_entities = usuario_service.obtener_todos_los_usuarios()
    if usuario_entities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuarios no encontrados"
        )
    return UsuarioMapper.to_schema_list(usuario_entities)


@router.get("/{id}", response_model=UsuarioResponseSchema)
def obtener_usuario_por_id(id: int):
    """Obtiene un usuario por su identificador.

    Args:

        id: Identificador del usuario.

    Returns:

        Usuario convertido a su esquema de respuesta.

    Raises:

        HTTPException: Si no se encuentra el usuario.
    """
    usuario_entity = usuario_service.obtener_usuario_por_id(id)
    if usuario_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
        )
    return UsuarioMapper.to_schema(usuario_entity)