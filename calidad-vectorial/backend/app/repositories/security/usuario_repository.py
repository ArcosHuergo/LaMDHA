from app.config.database import with_db
from app.models.security.usuario import Usuario


class UsuarioRepository:
    """Repositorio para gestionar usuarios en la base de datos."""

    @with_db
    def find_all(self, db) -> list[Usuario]:
        """Obtiene todos los usuarios.

        Args:
            db: Sesión de base de datos.

        Returns:
            Lista de usuarios almacenados.
        """
        return db.query(Usuario).all()

    @with_db
    def find_by_id(self, db, id_usuario: int) -> Usuario | None:
        """Busca un usuario por su identificador.

        Args:
            db: Sesión de base de datos.
            id_usuario: Identificador del usuario.

        Returns:
            Usuario encontrado o None si no existe.
        """
        return db.query(Usuario).filter(Usuario.id == id_usuario).first()

    @with_db
    def find_by_username(self, db, username: str) -> Usuario | None:
        """Busca un usuario por su nombre de usuario.

        Args:
            db: Sesión de base de datos.
            username: Nombre de usuario a buscar.

        Returns:
            Usuario encontrado o None si no existe.
        """
        return db.query(Usuario).filter(Usuario.username == username).first()

    @with_db
    def delete(self, db, usuario: Usuario) -> bool:
        """Elimina un usuario de la base de datos.

        Args:
            db: Sesión de base de datos.
            usuario: Usuario que se desea eliminar.

        Returns:
            True si el usuario fue eliminado; False si no existe.
        """
        usuario_a_eliminar = self.find_by_id(usuario.id)
        if not usuario_a_eliminar:
            return False
        db.delete(usuario_a_eliminar)
        db.commit()
        return True

    @with_db
    def insert(self, db, usuario: Usuario) -> Usuario:
        """Inserta un usuario en la base de datos.

        Args:
            db: Sesión de base de datos.
            usuario: Usuario que se desea insertar.

        Returns:
            Usuario insertado y actualizado con sus datos persistidos.
        """
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
