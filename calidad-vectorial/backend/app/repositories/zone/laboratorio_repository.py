from app.config.database import with_db
from app.models.zone.laboratorio import Laboratorio


class LaboratorioRepository:
    @with_db
    def find_all(self, db) -> list[Laboratorio]:
        return db.query(Laboratorio).all()

    @with_db
    def find_by_id(self, db, id_laboratorio: int) -> Laboratorio | None:
        return db.query(Laboratorio).filter(Laboratorio.id == id_laboratorio).first()

    @with_db
    def find_by_nombre(self, db, nombre: str) -> Laboratorio | None:
        return db.query(Laboratorio).filter(Laboratorio.nombre == nombre).first()
