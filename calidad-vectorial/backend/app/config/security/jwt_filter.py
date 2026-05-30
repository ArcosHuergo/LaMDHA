from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.services.security.jwt_service import jwt_service

PUBLIC_PATHS = {"/auth/login", "/auth/logout", "/docs", "/auth/register"}

class JwtAuthFilter(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str | None:
        # Rutas públicas
        if request.url.path in PUBLIC_PATHS:
            return None

        token = None

        # 1) Intentar desde el header Authorization: Bearer <token>
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            if credentials:
                token = credentials.credentials
        except Exception:
            pass

        # 2) Si no hay header, buscar en la cookie
        if token is None:
            token = request.cookies.get("JWT_TOKEN")

        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token no encontrado."
            )

        # 3) Validar token
        try:
            username = jwt_service.extraer_username(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado."
            )

        if not jwt_service.validar_token(token, username):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )

        # 4) Inyectar el username en el request para usarlo en los endpoints
        request.state.username = username
        return username