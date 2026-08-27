from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class HojaRegistro(Base):
    __tablename__ = "hoja_registro"

    id = Column(Integer, primary_key=True, index=True)

    #Registro muchos a uno
    registro_id = Column(Integer, ForeignKey("registro.id"), unique=True)
    registro = relationship("Registro", back_populates="hoja_registro")

    #aula uno a uno
    aula_id = Column(Integer, ForeignKey("aula.id"), unique=True, nulleable=True)
    aula = relationship("Aula", back_populates="hoja_registro")

    #pasillo uno a uno
    pasillo_id = Column(Integer, ForeignKey("pasillo.id"), unique=True, nulleable=True)
    pasillo = relationship("Pasillo", back_populates="hoja_registro", uselist=False)

    #patio uno a uno
    patio_id = Column(Integer, ForeignKey("patio.id"), unique=True, nulleable=True)
    patio = relationship("Patio", back_populates="hoja_registro", uselist=False)

    confianza = Column(Numeric(5, 2), unique=True, nullable=False)