from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Patio(Base):
    """Representa un patio dentro de una zona del sistema."""

    __tablename__ = "patio"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre identificador del patio
    nombre = Column(String(150), unique=True, nullable=False)

    # Referencia o código identificador del patio
    referencia = Column(String(10), nullable=False)

    # Descripción de las características o ubicación del patio
    descripcion = Column(String(255), nullable=False)

    # Zona a la que pertenece el patio
    zona_id = Column(Integer, ForeignKey("zona.id"), unique=True)
    zona = relationship("Zona", back_populates="patio")

    hoja_registro = relationship("HojaRegistro", back_populates="patio")
