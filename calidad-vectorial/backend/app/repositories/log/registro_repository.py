from app.config.database import with_db
from app.models.log.registro import Registro


class RegistroRepository:
    """Repositorio para gestionar registros en la base de datos."""

    @with_db
    def insert(self, db, registro: Registro) -> Registro:
        """Inserta un registro en la base de datos.

        Args:
            db: Sesión de base de datos.
            registro: Registro que se desea insertar.

        Returns:
            Registro insertado y actualizado con sus datos persistidos.
        """
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro

    @with_db
    def find_by_id(self, db, id_registro: int) -> Registro | None:
        """Busca un registro por su identificador.

        Args:
            db: Sesión de base de datos.
            id_registro: Identificador del registro.

        Returns:
            Registro encontrado o None si no existe.
        """
        return db.query(Registro).filter(Registro.id == id_registro).first()

    @with_db
    def find_all_by_usuario_id(self, db, id_usuario: int) -> Registro | None:
        """Obtiene los registros asociados a un usuario.

        Args:
            db: Sesión de base de datos.
            id_usuario: Identificador del usuario.

        Returns:
            Lista de registros asociados al usuario.
        """
        return db.query(Registro).filter(Registro.usuario_id == id_usuario).all()

    @with_db
    def update(self, db, registro: Registro) -> Registro:
        """Actualiza un registro existente en la base de datos.

        Args:
            db: Sesión de base de datos.
            registro: Registro con los datos actualizados.

        Returns:
            Registro actualizado y persistido.
        """
        registro = db.merge(registro)
        db.commit()
        db.refresh(registro)
        return registro
