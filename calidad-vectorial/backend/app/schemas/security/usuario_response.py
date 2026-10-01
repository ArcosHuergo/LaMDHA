from pydantic import BaseModel


class UsuarioResponseSchema(BaseModel):
    nickname: str
    username: str
