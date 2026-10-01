from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Biblioteca(Base):
    """Representa una biblioteca dentro de una zona del sistema."""

    __tablename__ = "biblioteca"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre identificador de la biblioteca
    nombre = Column(String(150), unique=True, nullable=False)

    # Referencia o código identificador de la biblioteca
    referencia = Column(String(20), nullable=False)

    # Descripción de las características o ubicación de la biblioteca
    descripcion = Column(String(255), nullable=False)

    # Zona a la que pertenece la biblioteca
    zona_id = Column(Integer, ForeignKey("zona.id"), unique=True)
    zona = relationship("Zona", back_populates="biblioteca")

    hoja_registro = relationship("HojaRegistro", back_populates="biblioteca")
