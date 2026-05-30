from fastapi import APIRouter, Depends, HTTPException, Response, Request, status

from app.services.security.jwt_service import jwt_service
from app.config.security.jwt_filter import JwtAuthFilter
from app.schemas.security.login import LoginSchema
from app.schemas.security.register import RegisterSchema
from app.services.security.usuario_service import UsuarioService
from app.mappers.security.usuario_mapper import UsuarioMapper

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_usuario_service() -> UsuarioService:
    return UsuarioService()

@router.post("/login", status_code = status.HTTP_201_CREATED)
def login(request_data: LoginSchema, response: Response, usuario_service: UsuarioService = Depends(get_usuario_service)):
    
    # 1) Verificar que el usuario exista
    usuario = usuario_service.obtener_usuario_por_username(request_data.username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")

    # 2) Verificar contraseña
    if not usuario_service.validar_password(request_data.password, usuario.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")

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
        max_age=3600,
        path="/",
    )

    # 5) También devolver el token en el body
    return {"token": token}


@router.post("/register", status_code = status.HTTP_201_CREATED)
def registrar(RegisterSchema: RegisterSchema, usuario_service: UsuarioService = Depends(get_usuario_service)): 
    usuario = UsuarioMapper.to_entity(RegisterSchema)
    nuevo_usuario = usuario_service.registrar_usuario(usuario ,RegisterSchema.password, RegisterSchema.verification_password)
    nuevo_usuarioDTO = UsuarioMapper.to_schema(nuevo_usuario)
    return nuevo_usuarioDTO


@router.get("/validar-token")
def validar_token(request: Request, _: str = Depends(JwtAuthFilter)):
    return {"detail": "Token válido", "username": request.state.username}


@router.post("/logout", status_code = status.HTTP_201_CREATED)
def logout(response: Response):
    response.delete_cookie(key="JWT_TOKEN", path="/")
    return {"detail": "Logout exitoso"}