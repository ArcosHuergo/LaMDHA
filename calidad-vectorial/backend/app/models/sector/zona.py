from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class Zona(Base):
    __tablename__ = "zona"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String(15), unique=True, nullable=False)

    #aula uno a muchos
    aula = relationship("Aula", back_populates="zona")

    #laboratorio uno a muchos
    laboratorio = relationship("Laboratorio", back_populates="zona")

    #pasillo uno a uno
    pasillo = relationship("Pasillo", back_populates="zona", uselist=False)

    #patio 
    patio = relationship("Patio", back_populates="zona", uselist=False)