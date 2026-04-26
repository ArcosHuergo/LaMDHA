from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from contextlib import contextmanager
from functools import wraps
from app.config.settings import settings

DATABASE_URL = (
    f"mysql+pymysql://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

# Conexión con la base de datos en MySQL
engine = create_engine(DATABASE_URL, echo=True)

# Fábrica de sesiones: autocommit/autoflush en False para control manual, expire_on_commit=False para que los objetos retengan sus datos al cerrar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# Maneja las sesiones con la base de datos
@contextmanager
def get_db():
    db = SessionLocal() # Abre la sesión
    try:
        yield db
        db.commit() # Guarda cambios
    except Exception:
        db.rollback() # Vuelve para atrás ante un error
        raise
    finally:
        db.close() # Cierra la sesión

# Decorador que inyecta la sesión de BD en los repositories
def with_db(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with get_db() as db:
            return func(self, db, *args, **kwargs)
    return wrapper