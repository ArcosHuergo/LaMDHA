from app.config.database import with_db
from app.models.zone.aula import Aula


class AulaRepository:
    """Repositorio para gestionar aulas en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Aula]:
        """Obtiene todas las aulas.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de aulas almacenadas.
        """
        return db.query(Aula).all()

    @with_db
    def find_by_id(self, db, id_aula: int) -> Aula | None:
        """Busca un aula por su identificador.

        Args:
            db: Sesión de base de datos.
            id_aula: Identificador del aula.

        Returns:
            Aula encontrada o None si no existe.
        """
        return db.query(Aula).filter(Aula.id == id_aula).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Aula | None:
        """Busca un aula por su nombre.

        Args:
            db: Sesión de base de datos.
            nombre: Nombre del aula a buscar.

        Returns:
            Aula encontrada o None si no existe.
        """
        return db.query(Aula).filter(Aula.nombre == nombre).first()
