from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def registrar(self, usuario: Usuario, password: str, verification_password: str) -> Usuario:
        if (password != verification_password):
            raise ValueError("Las contraseñas no coinciden")
        
        if (UsuarioRepository.find_by_username(usuario.username) is not None):
            raise ValueError("El nombre del usuario ya existe")
        
        usuario.password = pwd_context.hash(password)
        return UsuarioRepository.insert(usuario)
    
    def obtener_todos_usuarios(self) -> list[Usuario]:
        return self.repo.find_all()

    def obtener_usuario_por_id(self, id: int) -> Usuario:
        return self.repo.find_by_id(id)

    def eliminar_usuario(self, usuario: Usuario):
        self.repo.delete(usuario)
