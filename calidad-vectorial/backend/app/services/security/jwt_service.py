from datetime import datetime, timedelta, timezone

from app.config.settings import settings
from jose import JWTError, jwt


class JwtService:
    def __init__(self):
        self.secret = settings.jwt_secret
        self.algorithm = "HS256"
        self.expiration = settings.jwt_expiration_ms

    def generar_token(self, username: str, roles: list[str]) -> str:
        """Genera un token JWT para un usuario.

        Args:
            username: Nombre de usuario que se incluirá en el token.
            roles: Lista de roles asociados al usuario.

        Returns:
            Token JWT firmado y con fecha de expiración.
        """
        now = datetime.now(timezone.utc)
        expiry = now + timedelta(milliseconds=self.expiration)

        payload = {
            "sub": username,
            "roles": roles,
            "iat": now,
            "exp": expiry,
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def extraer_username(self, token: str) -> str:
        """Extrae el nombre de usuario contenido en un token JWT.

        Args:
            token: Token JWT que se desea decodificar.

        Returns:
            Nombre de usuario contenido en el campo `sub` del token.
        """
        payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        return payload.get("sub")

    def validar_token(self, token: str, username: str) -> bool:
        """Valida un token JWT y verifica el usuario asociado.

        Args:
            token: Token JWT que se desea validar.
            username: Nombre de usuario esperado en el token.

        Returns:
            True si el token es válido y pertenece al usuario indicado.
            False si el token es inválido o pertenece a otro usuario.
        """
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            sub = payload.get("sub")
            return sub is not None and sub == username
        except JWTError:
            return False


jwt_service = JwtService()
