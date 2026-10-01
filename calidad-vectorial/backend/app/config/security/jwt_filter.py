from app.services.security.jwt_service import jwt_service
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Rutas públicas sin ningún tipo de autenticación
PUBLIC_PATHS = {"/auth/login", "/auth/logout", "/docs", "/auth/register"}

# Rutas públicas que admiten token pero funcionan anonimante de no haberlo
OPTIONAL_AUTH_PATHS = {"/vision/ubicacion"}


class JwtAuthFilter(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def _extraer_token(self, request: Request) -> str | None:
        # 1) Header Authorization: Bearer <token>
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            if credentials:
                return credentials.credentials
        except Exception:
            pass
        # 2) Cookie
        return request.cookies.get("JWT_TOKEN")

    async def __call__(self, request: Request) -> str | None:
        path = request.url.path

        if path in PUBLIC_PATHS:
            return None

        token = await self._extraer_token(request)

        # Autenticación opcional: si hay token válido se identifica, si no, anónimo
        if path in OPTIONAL_AUTH_PATHS:
            if token is not None:
                try:
                    username = jwt_service.extraer_username(token)
                    if jwt_service.validar_token(token, username):
                        request.state.username = username
                        return username
                except Exception:
                    pass
            return None

        # Autenticación obligatoria
        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no encontrado."
            )

        try:
            username = jwt_service.extraer_username(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado.",
            )

        if not jwt_service.validar_token(token, username):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido."
            )

        request.state.username = username
        return username
