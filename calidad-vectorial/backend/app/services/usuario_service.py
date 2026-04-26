from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def obtener_todos_usuarios(self) -> list[Usuario]:
        return self.repo.find_all()

    def obtener_usuario_por_id(self, id: int) -> Usuario:
        return self.repo.find_by_id(id)

    def eliminar_usuario(self, usuario: Usuario):
        self.repo.delete(usuario)