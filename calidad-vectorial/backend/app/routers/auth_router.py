from fastapi import APIRouter, Depends, HTTPException, Response, Request, status

from app.services.jwt_service import JwtService
from app.config.security.jwt_filter import JwtAuthFilter
from app.dto.login_dto import LoginDTO
from app.services.usuario_service import UsuarioService

router     = APIRouter(prefix="/auth", tags=["Auth"])
jwt_service = JwtService()
jwt_filter  = JwtAuthFilter()

def get_usuario_service() -> UsuarioService:
    return UsuarioService()  # inyectá el repo como lo tengas

@router.post("/login")
def login(
    request_data: LoginDTO,
    response: Response,
    service: UsuarioService = Depends(get_usuario_service)
    ):
    
    # 1) Verificar que el usuario exista
    usuario = service.find_by_username(request_data.username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado.")

    # 2) Verificar contraseña
    if not service.verify_password(request_data.password, usuario.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")

    # 3) Generar token
    roles = usuario.roles if hasattr(usuario, "roles") else []
    token = jwt_service.generar_token(usuario.username, roles)

    # 4) Cookie HTTP-only (igual que Spring)
    response.set_cookie(
        key="JWT_TOKEN",
        value=token,
        httponly=True,       # Previene acceso desde JS (XSS)
        secure=False,        # True en producción (HTTPS)
        samesite="lax",
        max_age=3600,
        path="/",
    )

    # 5) También devolver el token en el body
    return {"token": token}


@router.get("/validar-token")
def validar_token(
    request: Request,
    _: str = Depends(jwt_filter)  # el filtro ya valida, si llega acá es válido
):
    return {"detail": "Token válido", "username": request.state.username}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="JWT_TOKEN", path="/")
    return {"detail": "Logout exitoso"}