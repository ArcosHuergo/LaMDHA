from app.models.security.usuario import Usuario
from app.repositories.security.usuario_repository import UsuarioRepository
import bcrypt


class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def obtener_todos_usuarios(self) -> list[Usuario]:
        return self.usuario_repository.find_all()

    def obtener_usuario_por_id(self, id: int) -> Usuario:
        return self.usuario_repository.find_by_id(id)
    
    def obtener_usuario_por_username(self, username: str) -> Usuario:
        return self.usuario_repository.find_by_username(username)

    def eliminar_usuario(self, usuario: Usuario):
        self.usuario_repository.delete(usuario)

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def registrar_usuario(self, usuario: Usuario, password: str, verification_password: str) -> Usuario:
        if (password != verification_password):
            raise ValueError("Las contraseñas no coinciden")
        
        if (self.usuario_repository.find_by_username(usuario.username) is not None):
            raise ValueError("El nombre del usuario ya existe")
        
        usuario.password = self.hash_password(password)
        return self.usuario_repository.insert(usuario)

    def validar_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))