from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class HojaRegistro(Base):
    __tablename__ = "hoja_registro"

    id = Column(Integer, primary_key=True, index=True)

    #Registro muchos a uno
    registro_id = Column(Integer, ForeignKey("registro.id"), nullable=False)
    registro = relationship("Registro", back_populates="hoja_registro")

    #aula uno a uno
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=True)
    aula = relationship("Aula", back_populates="hoja_registro")

    #pasillo uno a uno
    pasillo_id = Column(Integer, ForeignKey("pasillo.id"), nullable=True)
    pasillo = relationship("Pasillo", back_populates="hoja_registro", uselist=False)

    #patio uno a uno
    patio_id = Column(Integer, ForeignKey("patio.id"), nullable=True)
    patio = relationship("Patio", back_populates="hoja_registro", uselist=False)

    confianza = Column(Numeric(5, 4), nullable=False)