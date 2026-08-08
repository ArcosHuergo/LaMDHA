from app.config.database import with_db
from app.models.zone.aula import Aula

class AulaRepository:

    @with_db
    def find_all(self, db) -> list[Aula]:
        return db.query(Aula).all()
    
    @with_db
    def find_by_id(self, db, id_aula: int) -> Aula | None:
        return db.query(Aula).filter(Aula.id == id_aula).first()
