from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Laboratorio(Base):
    """Representa un laboratorio dentro de una zona del sistema."""

    __tablename__ = "laboratorio"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre identificador del laboratorio
    nombre = Column(String(150), nullable=False, unique=True)

    # Referencia o código identificador del laboratorio
    referencia = Column(String(10), nullable=False)

    # Descripción de las características o ubicación del laboratorio
    descripcion = Column(String(255), nullable=False)

    # Zona a la que pertenece el laboratorio
    zona_id = Column(Integer, ForeignKey("zona.id"), nullable=False)
    zona = relationship("Zona", back_populates="laboratorio")

    hoja_registro = relationship("HojaRegistro", back_populates="laboratorio")
