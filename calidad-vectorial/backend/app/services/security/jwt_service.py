from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config.settings import settings

class JwtService:
    def __init__(self):
        self.secret     = settings.jwt_secret
        self.algorithm  = "HS256"
        self.expiration = settings.jwt_expiration_ms

    def generar_token(self, username: str, roles: list[str]) -> str:
        now    = datetime.now(timezone.utc)
        expiry = now + timedelta(milliseconds=self.expiration)

        payload = {
            "sub":   username,
            "roles": roles,
            "iat":   now,
            "exp":   expiry,
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def extraer_username(self, token: str) -> str:
        payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        return payload.get("sub")

    def validar_token(self, token: str, username: str) -> bool:
        try:
            payload  = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            sub      = payload.get("sub")
            return sub is not None and sub == username
        except JWTError:
            return False

jwt_service = JwtService()