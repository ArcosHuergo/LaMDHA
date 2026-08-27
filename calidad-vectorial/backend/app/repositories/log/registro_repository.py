from app.config.database import with_db
from app.models.log.registro import Registro

class RegistroRepository:

    @with_db
    def insert(self, db, registro: Registro) -> Registro:
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro