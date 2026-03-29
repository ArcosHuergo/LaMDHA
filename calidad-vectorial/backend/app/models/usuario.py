from pydantic import BaseModel, Field

class Usuario(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=20)