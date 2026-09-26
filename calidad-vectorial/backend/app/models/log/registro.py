from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, String, func
from sqlalchemy.orm import relationship
from app.config.database import Base

class Registro(Base):
    __tablename__ = "registro"

    id = Column(Integer, primary_key=True, index=True)

    # hoja_registro uno a muchos
    hoja_registro = relationship("HojaRegistro", back_populates="registro")

    # usuario muchos a 1
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="registro")

    url_foto = Column(String(255), nullable=True)

    prediccion_correcta = Column(Boolean, nullable=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)