from app.config.database import with_db
from app.models.zone.biblioteca import Biblioteca


class BibliotecaRepository:
    """Repositorio para gestionar bibliotecas en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Biblioteca]:
        """Obtiene todas las bibliotecas.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de bibliotecas almacenadas.
        """
        return db.query(Biblioteca).all()

    @with_db
    def find_by_id(
        self, db, id_biblioteca: int
    ) -> Biblioteca | None:
        """Busca una biblioteca por su identificador.

        Args:
            db: Sesión de base de datos.
            id_biblioteca: Identificador de la biblioteca.

        Returns:
            Biblioteca encontrada o None si no existe.
        """
        return db.query(Biblioteca).filter(Biblioteca.id == id_biblioteca).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Biblioteca | None:
        """Busca una biblioteca por su nombre.

        Args:
            db: Sesión de base de datos.
            nombre: Nombre de la biblioteca a buscar.

        Returns:
            Biblioteca encontrada o None si no existe.
        """
        return db.query(Biblioteca).filter(Biblioteca.nombre == nombre).first()
