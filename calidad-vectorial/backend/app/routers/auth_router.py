from fastapi import APIRouter, Depends, HTTPException, Response, Request, status

from app.services.jwt_service import jwt_service
from app.config.security.jwt_filter import JwtAuthFilter
from app.dto.login_dto import LoginDTO
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_usuario_service() -> UsuarioService:
    return UsuarioService()

@router.post("/login")
def login(request_data: LoginDTO, response: Response, usuario_service: UsuarioService = Depends(get_usuario_service)):
    
    # 1) Verificar que el usuario exista
    usuario = usuario_service.obtener_usuario_por_id(request_data.username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")

    # 2) Verificar contraseña
    if not usuario_service.validar_password(request_data.password, usuario.hashed_password):
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


@router.get("/validar-token")
def validar_token(request: Request, _: str = Depends(JwtAuthFilter)):
    return {"detail": "Token válido", "username": request.state.username}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="JWT_TOKEN", path="/")
    return {"detail": "Logout exitoso"}