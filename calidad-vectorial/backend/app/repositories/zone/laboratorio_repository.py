from app.config.database import with_db
from app.models.zone.laboratorio import Laboratorio


class LaboratorioRepository:
    """Repositorio para gestionar laboratorios en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Laboratorio]:
        """Obtiene todos los laboratorios.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de laboratorios almacenados.
        """
        return db.query(Laboratorio).all()

    @with_db
    def find_by_id(
        self, db, id_laboratorio: int
    ) -> Laboratorio | None:
        """Busca un laboratorio por su identificador.

        Args:
            db: Sesión de base de datos.
            id_laboratorio: Identificador del laboratorio.

        Returns:
            Laboratorio encontrado o None si no existe.
        """
        return db.query(Laboratorio).filter(Laboratorio.id == id_laboratorio).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Laboratorio | None:
        """Busca un laboratorio por su nombre.

        Args:
            db: Sesión de base de datos.
            nombre: Nombre del laboratorio a buscar.

        Returns:
            Laboratorio encontrado o None si no existe.
        """
        return db.query(Laboratorio).filter(Laboratorio.nombre == nombre).first()
