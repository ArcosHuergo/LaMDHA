from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Aula(Base):
    _tablename_ = "aula"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), unique=True, nullable=False)
    referencia = Column(String(2), unique=True, nullable=False)
    descripcion = Column(String(255), unique=True, nullable=False)

    #aula
    aula_id = Column(Integer, ForeignKey("aula.id"), nullable=False)
    aula = relationship("Zona", back_populates="aulas")