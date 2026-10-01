from pydantic import BaseModel


class ZonaResponseSchema(BaseModel):
    id: int
    color: str
