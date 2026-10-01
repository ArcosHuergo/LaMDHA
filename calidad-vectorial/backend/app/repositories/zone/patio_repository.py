from app.config.database import with_db
from app.models.zone.patio import Patio


class PatioRepository:
    @with_db
    def find_all(self, db) -> list[Patio]:
        return db.query(Patio).all()

    @with_db
    def find_by_id(self, db, id_patio: int) -> Patio | None:
        return db.query(Patio).filter(Patio.id == id_patio).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Patio | None:
        return db.query(Patio).filter(Patio.nombre == nombre).first()
