from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Biblioteca(Base):
    __tablename__ = "biblioteca"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), unique=True, nullable=False)
    referencia = Column(String(20), unique=True, nullable=False)
    descripcion = Column(String(255), unique=True, nullable=False)

    zona_id = Column(Integer, ForeignKey("zona.id"), unique=True)
    zona = relationship("Zona", back_populates="biblioteca")

    hoja_registro = relationship("HojaRegistro", back_populates="biblioteca")