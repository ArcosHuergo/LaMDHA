from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Aula(Base):
    __tablename__ = "aula"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False, unique=True)
    referencia = Column(String(10), nullable=False)
    descripcion = Column(String(255), nullable=False)

    # aula
    zona_id = Column(Integer, ForeignKey("zona.id"), nullable=False)
    zona = relationship("Zona", back_populates="aula")

    hoja_registro = relationship("HojaRegistro", back_populates="aula")
