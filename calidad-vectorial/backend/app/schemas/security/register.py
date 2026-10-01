import re

from pydantic import BaseModel, field_validator


class RegisterSchema(BaseModel):
    username: str
    password: str
    verification_password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if value is not None and not re.match(
            r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!*]).*$", value
        ):
            raise ValueError(
                "La contraseña debe contener al menos una mayúscula, una minúscula, un número y un carácter especial."
            )
        return value

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise ValueError("El username debe ser un email válido.")
        return value
