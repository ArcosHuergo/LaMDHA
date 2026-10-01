from app.config.database import with_db
from app.models.zone.pasillo import Pasillo


class PasilloRepository:
    """Repositorio para gestionar pasillos en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Pasillo]:
        """Obtiene todos los pasillos.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de pasillos almacenados.
        """
        return db.query(Pasillo).all()

    @with_db
    def find_by_id(self, db, id_pasillo: int) -> Pasillo | None:
        """Busca un pasillo por su identificador.

        Args:
            db: Sesión de base de datos.
            id_pasillo: Identificador del pasillo.

        Returns:
            Pasillo encontrado o None si no existe.
        """
        return db.query(Pasillo).filter(Pasillo.id == id_pasillo).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Pasillo | None:
        """Busca un pasillo por su nombre.

        Args:
            db: Sesión de base de datos.
            nombre: Nombre del pasillo a buscar.

        Returns:
            Pasillo encontrado o None si no existe.
        """
        return db.query(Pasillo).filter(Pasillo.nombre == nombre).first()
