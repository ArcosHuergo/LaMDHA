from pydantic import BaseModel

class LoginDTO(BaseModel):
    nickame: str
    username: str
    password: str