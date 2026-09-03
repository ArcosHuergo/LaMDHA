from app.config.database import with_db
from app.models.zone.biblioteca import Biblioteca

class BibliotecaRepository:

    @with_db
    def find_all(self, db) -> list[Biblioteca]:
        return db.query(Biblioteca).all()
    
    @with_db
    def find_by_id(self, db, id_biblioteca: int) -> Biblioteca | None:
        return db.query(Biblioteca).filter(Biblioteca.id == id_biblioteca).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Biblioteca | None:
        return db.query(Biblioteca).filter(Biblioteca.nombre == nombre).first()