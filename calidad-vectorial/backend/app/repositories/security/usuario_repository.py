from app.config.database import with_db
from app.models.security.usuario import Usuario


class UsuarioRepository:
    @with_db
    def find_all(self, db) -> list[Usuario]:
        return db.query(Usuario).all()

    @with_db
    def find_by_id(self, db, id_usuario: int) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.id == id_usuario).first()

    @with_db
    def find_by_username(self, db, username: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.username == username).first()

    @with_db
    def delete(self, db, usuario: Usuario) -> bool:
        usuario_a_eliminar = self.find_by_id(usuario.id)
        if not usuario_a_eliminar:
            return False
        db.delete(usuario_a_eliminar)
        db.commit()
        return True

    @with_db
    def insert(self, db, usuario: Usuario) -> Usuario:
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
