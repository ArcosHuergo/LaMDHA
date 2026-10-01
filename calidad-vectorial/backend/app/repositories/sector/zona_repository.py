from app.config.database import with_db
from app.models.sector.zona import Zona


class ZonaRepository:
    """Repositorio para gestionar zonas en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Zona]:
        """Obtiene todas las zonas.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de zonas almacenadas.
        """
        return db.query(Zona).all()

    @with_db
    def find_by_id(self, db, id_zona: int) -> Zona | None:
        """Busca una zona por su identificador.

        Args:
            db: Sesión de base de datos.
            id_zona: Identificador de la zona.

        Returns:
            Zona encontrada o None si no existe.
        """
        return db.query(Zona).filter(Zona.id == id_zona).first()
