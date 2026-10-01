from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Pasillo(Base):
    """Representa un pasillo dentro de una zona del sistema."""

    __tablename__ = "pasillo"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre identificador del pasillo
    nombre = Column(String(150), unique=True, nullable=False)

    # Descripción de las características o ubicación del pasillo
    descripcion = Column(String(255), nullable=False)

    # Zona a la que pertenece el pasillo
    zona_id = Column(Integer, ForeignKey("zona.id"), unique=True)
    zona = relationship("Zona", back_populates="pasillo")

    hoja_registro = relationship("HojaRegistro", back_populates="pasillo")
