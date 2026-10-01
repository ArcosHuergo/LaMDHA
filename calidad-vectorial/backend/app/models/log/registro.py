from app.config.database import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class Registro(Base):
    """Representa un registro de una clasificación realizada."""

    __tablename__ = "registro"

    # ID principal de la entidad
    id = Column(Integer, primary_key=True, index=True)

    # Hoja de registro: relación uno a muchos
    hoja_registro = relationship("HojaRegistro", back_populates="registro")

    # Usuario: relación muchos a uno
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="registro")

    # Foto subida porel usuario
    url_foto = Column(String(255), nullable=True)

    # Feedback del usuario si la prediccion fue correcta
    prediccion_correcta = Column(Boolean, nullable=True)

    # La fecha de creacion del registro
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
