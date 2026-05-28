from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def obtener_todos_usuarios(self) -> list[Usuario]:
        return self.repo.find_all()

    def obtener_usuario_por_id(self, id: int) -> Usuario:
        return self.repo.find_by_id(id)

    def eliminar_usuario(self, usuario: Usuario):
        self.repo.delete(usuario)

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def registrar(self, usuario: Usuario, password: str, verification_password: str) -> Usuario:
        if (password != verification_password):
            raise ValueError("Las contraseñas no coinciden")
        
        if (UsuarioRepository.find_by_username(usuario.username) is not None):
            raise ValueError("El nombre del usuario ya existe")
        
        usuario.password = self.hash_password(password)
        return UsuarioRepository.insert(usuario)

    def validar_password(self, password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)