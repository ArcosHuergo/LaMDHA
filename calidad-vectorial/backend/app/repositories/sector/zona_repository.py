from app.config.database import with_db
from app.models.sector.zona import Zona

class ZonaRepository:

    with_db
    def find_all(self, db) -> list[Zona]:
        return db.query(Zona).all()
    
    @with_db
    def find_by_id(self, db, id_zona: int) -> Zona | None:
        return db.query(Zona).filter(Zona.id == id_zona).first()