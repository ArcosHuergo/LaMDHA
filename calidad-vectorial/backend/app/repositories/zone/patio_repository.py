from app.config.database import with_db
from app.models.zone.patio import Patio


class PatioRepository:
    """Repositorio para gestionar patios en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Patio]:
        """Obtiene todos los patios.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de patios almacenados.
        """
        return db.query(Patio).all()

    @with_db
    def find_by_id(self, db, id_patio: int) -> Patio | None:
        """Busca un patio por su identificador.

        Args:
            db: Sesión de base de datos.
            id_patio: Identificador del patio.

        Returns:
            Patio encontrado o None si no existe.
        """
        return db.query(Patio).filter(Patio.id == id_patio).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Patio | None:
        """Busca un patio por su nombre.

        Args:
            db: Sesión de base de datos.
            nombre: Nombre del patio a buscar.

        Returns:
            Patio encontrado o None si no existe.
        """
        return db.query(Patio).filter(Patio.nombre == nombre).first()
