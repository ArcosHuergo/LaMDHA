from app.config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Zona(Base):
    """Representa una zona y sus sectores asociados."""

    __tablename__ = "zona"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Color designado a la zona
    color = Column(String(15), unique=True, nullable=False)

    # Aula: relación uno a muchos
    aula = relationship("Aula", back_populates="zona")

    # Laboratorio: relación uno a muchos
    laboratorio = relationship("Laboratorio", back_populates="zona")

    # Pasillo: relación uno a uno
    pasillo = relationship("Pasillo", back_populates="zona", uselist=False)

    # Patio: relación uno a uno
    patio = relationship("Patio", back_populates="zona", uselist=False)

    # Biblioteca: relación uno a uno
    biblioteca = relationship("Biblioteca", back_populates="zona", uselist=False)
