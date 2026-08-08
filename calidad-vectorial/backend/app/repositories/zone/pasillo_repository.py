from app.config.database import with_db
from app.models.zone.pasillo import Pasillo

class PasilloRepository:

    @with_db
    def find_all(self, db) -> list[Pasillo]:
        return db.query(Pasillo).all()
    
    @with_db
    def find_by_id(self, db, id_pasillo: int) -> Pasillo | None:
        return db.query(Pasillo).filter(Pasillo.id == id_pasillo).first()

