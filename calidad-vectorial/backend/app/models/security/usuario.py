from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, nullable=False)
    nickname = Column(String(100), nullable=False)
    password = Column(String(64), nullable=False)