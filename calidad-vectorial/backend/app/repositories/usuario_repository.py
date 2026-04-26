from app.config.database import with_db
from app.models.usuario import Usuario

class UsuarioRepository:

    @with_db
    def find_all(self, db) -> list[Usuario]:
        return db.query(Usuario).all()

    @with_db
    def find_by_id(self, db, id_usuario: int) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.id == id_usuario).first()

    @with_db
    def find_by_username(self, db, email: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.username == email).first()

    @with_db
    def delete(self, db, usuario: Usuario) -> bool:
        usuario_a_eliminar = db.find_by_id(usuario.id)
        if not usuario_a_eliminar:
            return False
        self.db.delete(usuario_a_eliminar)
        self.db.commit()
        return True