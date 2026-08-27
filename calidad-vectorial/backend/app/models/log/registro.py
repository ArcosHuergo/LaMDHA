from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class Registro(Base):
    __tablename__ = "registro"

    id = Column(Integer, primary_key=True, index=True)

    # hoja_registro uno a muchos
    hoja_registro = relationship("Hoja_Registro", back_populates="registro")

    # usuario muchos a 1
    usuario_id = Column(Integer, ForeignKey("usuario.id"), unique=True)
    usuario = relationship("Usuario", back_populates="registro")

    url_foto = Column(String(255), unique=True, nullable=True)