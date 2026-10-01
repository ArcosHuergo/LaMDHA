import bcrypt

from app.models.security.usuario import Usuario
from app.repositories.security.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def obtener_todos_los_usuarios(self) -> list[Usuario]:
        """Obtiene todos los usuarios registrados.

        Returns:
            Lista de usuarios almacenados.
        """
        return self.usuario_repository.find_all()

    def obtener_usuario_por_id(self, id: int) -> Usuario:
        """Obtiene un usuario por su identificador.

        Args:
            id: Identificador del usuario.

        Returns:
            Usuario correspondiente al identificador.
        """
        return self.usuario_repository.find_by_id(id)

    def obtener_usuario_por_username(self, username: str) -> Usuario:
        """Obtiene un usuario por su nombre de usuario.

        Args:
            username: Nombre de usuario a buscar.

        Returns:
            Usuario correspondiente al nombre de usuario.
        """
        return self.usuario_repository.find_by_username(username)

    def eliminar_usuario(self, usuario: Usuario):
        """Elimina un usuario.

        Args:
            usuario: Usuario que se desea eliminar.
        """
        self.usuario_repository.delete(usuario)

    @staticmethod
    def hash_password(password: str) -> str:
        """Genera un hash seguro para una contraseña.

        Args:
            password: Contraseña en texto plano.

        Returns:
            Hash de la contraseña.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def registrar_usuario(
        self, usuario: Usuario, password: str, verification_password: str
    ) -> Usuario:
        """Registra un nuevo usuario después de validar sus datos.

        Args:
            usuario: Datos del usuario que se desea registrar.
            password: Contraseña del usuario.
            verification_password: Confirmación de la contraseña.

        Returns:
            Usuario registrado.

        Raises:
            ValueError: Si las contraseñas no coinciden o el nombre de usuario
                ya existe.
        """
        if password != verification_password:
            raise ValueError("Las contraseñas no coinciden")

        if self.usuario_repository.find_by_username(usuario.username) is not None:
            raise ValueError("El nombre del usuario ya existe")

        usuario.password = self.hash_password(password)
        return self.usuario_repository.insert(usuario)

    def validar_password(self, password: str, hashed_password: str) -> bool:
        """Valida una contraseña contra un hash almacenado.

        Args:
            password: Contraseña en texto plano.
            hashed_password: Hash con el que se compara la contraseña.

        Returns:
            True si la contraseña coincide con el hash; False en caso contrario.
        """
        return bcrypt.checkpw(
            password.encode("utf-8"), hashed_password.encode("utf-8")
        )
