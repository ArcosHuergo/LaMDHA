from pydantic import BaseModel

class RegisterDTO(BaseModel):
    nickame: str
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if value is not None and not re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!*]).*$", value):
            raise ValueError(
                "La contraseña debe contener al menos una mayúscula, una minúscula, un número y un carácter especial."
            )
        return value