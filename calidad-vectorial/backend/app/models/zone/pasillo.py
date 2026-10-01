from app.config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Pasillo(Base):
    __tablename__ = "pasillo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=False)

    zona_id = Column(Integer, ForeignKey("zona.id"), unique=True)
    zona = relationship("Zona", back_populates="pasillo")

    hoja_registro = relationship("HojaRegistro", back_populates="pasillo")
