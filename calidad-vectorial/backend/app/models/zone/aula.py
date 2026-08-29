from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Aula(Base):
    __tablename__ = "aula"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    referencia = Column(String(2), nullable=False)
    descripcion = Column(String(255), nullable=False)

    #aula
    zona_id = Column(Integer, ForeignKey("zona.id"), nullable=False)
    zona = relationship("Zona", back_populates="aula")

    hoja_registro = relationship("HojaRegistro", back_populates="aula")