from app.config.security.jwt_filter import JwtAuthFilter
from app.mappers.security.usuario_mapper import UsuarioMapper
from app.schemas.security.login import LoginSchema
from app.schemas.security.register import RegisterSchema
from app.schemas.security.usuario_response import UsuarioResponseSchema
from app.services.security.jwt_service import jwt_service
from app.services.security.usuario_service import UsuarioService
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_usuario_service() -> UsuarioService:
    """Obtiene una instancia del servicio de usuarios.

    Returns:

        Instancia de `UsuarioService`.
    """
    return UsuarioService()


@router.post("/login", status_code=status.HTTP_201_CREATED)
def login(
    login_schema: LoginSchema,
    response: Response,
    usuario_service: UsuarioService = Depends(get_usuario_service),
):
    """Autentica un usuario y genera un token JWT.

    Args:

        login_schema: Datos de acceso del usuario.
        response: Respuesta HTTP utilizada para establecer la cookie.
        usuario_service: Servicio utilizado para gestionar el usuario.

    Returns:

        Diccionario con el token JWT generado.

    Raises:
    
        HTTPException: Si las credenciales proporcionadas no son válidas.
    """
    # 1) Verificar que el usuario exista
    usuario = usuario_service.obtener_usuario_por_username(login_schema.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas."
        )

    # 2) Verificar contraseña
    if not usuario_service.validar_password(login_schema.password, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas."
        )

    # 3) Generar token
    roles = usuario.roles if hasattr(usuario, "roles") else []
    token = jwt_service.generar_token(usuario.username, roles)

    # 4) Cookie HTTP-only
    response.set_cookie(
        key="JWT_TOKEN",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=36000,
        path="/",
    )

    # 5) También devolver el token en el body
    return {"token": token}


@router.post("/register", status_code=status.HTTP_201_CREATED)
def registrar(
    RegisterSchema: RegisterSchema,
    usuario_service: UsuarioService = Depends(get_usuario_service),
):
    """Registra un nuevo usuario.

    Args:

        RegisterSchema: Datos necesarios para registrar al usuario.
        usuario_service: Servicio utilizado para gestionar el registro.

    Returns:

        Esquema con los datos del usuario registrado.
    """
    usuario = UsuarioMapper.to_entity(RegisterSchema)
    nuevo_usuario = usuario_service.registrar_usuario(
        usuario, RegisterSchema.password, RegisterSchema.verification_password
    )
    nuevo_usuario_schema = UsuarioMapper.to_schema(nuevo_usuario)
    return nuevo_usuario_schema


@router.get("/validar-token")
def validar_token(request: Request, _: str = Depends(JwtAuthFilter)):
    """Valida el token JWT del usuario autenticado.

    Args:

        request: Solicitud HTTP con la información del usuario autenticado.
        _: Dependencia que valida el token JWT.

    Returns:

        Información indicando que el token es válido y el usuario autenticado.
    """
    return {"detail": "Token válido", "username": request.state.username}


@router.get("/me", response_model=UsuarioResponseSchema)
def me(
    request: Request, usuario_service: UsuarioService = Depends(get_usuario_service)
):
    """Obtiene los datos del usuario autenticado.

    Args:

        request: Solicitud HTTP con la información del usuario autenticado.
        usuario_service: Servicio utilizado para obtener el usuario.

    Returns:

        Esquema con los datos del usuario autenticado.

    Raises:

        HTTPException: Si el usuario autenticado no existe.
    """
    usuario = usuario_service.obtener_usuario_por_username(request.state.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado."
        )
    return UsuarioMapper.to_schema(usuario)


@router.post("/logout", status_code=status.HTTP_201_CREATED)
def logout(response: Response):
    """Cierra la sesión eliminando la cookie de autenticación.

    Args:

        response: Respuesta HTTP utilizada para eliminar la cookie.

    Returns:

        Mensaje indicando que el cierre de sesión fue exitoso.
    """
    response.delete_cookie(key="JWT_TOKEN", path="/")
    return {"detail": "Logout exitoso"}
