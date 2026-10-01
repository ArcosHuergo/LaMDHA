from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Aula(Base):
    """Representa un aula dentro de una zona del sistema."""

    __tablename__ = "aula"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Nombre identificador del aula
    nombre = Column(String(150), nullable=False, unique=True)

    # Referencia o código identificador del aula
    referencia = Column(String(10), nullable=False)

    # Descripción de las características o ubicación del aula
    descripcion = Column(String(255), nullable=False)

    # Zona a la que pertenece el aula
    zona_id = Column(Integer, ForeignKey("zona.id"), nullable=False)
    zona = relationship("Zona", back_populates="aula")

    # Registros de clasificación asociados al aula: relación uno a muchos
    hoja_registro = relationship("HojaRegistro", back_populates="aula")
