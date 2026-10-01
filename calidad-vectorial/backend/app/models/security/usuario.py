from app.config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Usuario(Base):
    """Representa un usuario registrado en el sistema."""

    __tablename__ = "usuarios"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre de usuario utilizado para iniciar sesión
    username = Column(String(150), unique=True, nullable=False)

    # Nombre visible del usuario
    nickname = Column(String(100), nullable=False)

    # Contraseña del usuario almacenada de forma cifrada
    password = Column(String(64), nullable=False)

    # Registros realizados por el usuario: relación uno a muchos
    registro = relationship("Registro", back_populates="usuario")
