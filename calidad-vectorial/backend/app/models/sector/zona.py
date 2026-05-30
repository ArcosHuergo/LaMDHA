from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Zona(Base):
    _tablename_ = "zona"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String(15), unique=True, nullable=False)

    #aula uno a muchos
    aulas = relationship("Aula", back_populates="zona")

    #pasillo uno a uno
    pasillo = relationship("Pasillo", back_populates="zona", uselist=False)

    #patio
    patio = relationship("Patio", back_populates="zona", uselist=False)

    
