from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship


class HojaRegistro(Base):
    """Representa una predicción de ubicación asociada a un registro."""

    __tablename__ = "hoja_registro"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Registro muchos a uno
    registro_id = Column(Integer, ForeignKey("registro.id"), nullable=False)
    registro = relationship("Registro", back_populates="hoja_registro")

    # Aula uno a uno
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=True)
    aula = relationship("Aula", back_populates="hoja_registro")

    # Laboratorio uno a uno
    labo_id = Column(Integer, ForeignKey("laboratorio.id"), nullable=True)
    laboratorio = relationship("Laboratorio", back_populates="hoja_registro")

    # Pasillo uno a uno
    pasillo_id = Column(Integer, ForeignKey("pasillo.id"), nullable=True)
    pasillo = relationship("Pasillo", back_populates="hoja_registro", uselist=False)

    # Patio uno a uno
    patio_id = Column(Integer, ForeignKey("patio.id"), nullable=True)
    patio = relationship("Patio", back_populates="hoja_registro", uselist=False)

    # Biblioteca uno a uno
    biblioteca_id = Column(Integer, ForeignKey("biblioteca.id"), nullable=True)
    biblioteca = relationship(
        "Biblioteca", back_populates="hoja_registro", uselist=False
    )

    # Confianza que devolvio la red neuronal
    confianza = Column(Numeric(5, 4), nullable=False)
