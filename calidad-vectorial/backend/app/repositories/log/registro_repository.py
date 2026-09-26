from app.config.database import with_db
from app.models.log.registro import Registro

class RegistroRepository:

    @with_db
    def insert(self, db, registro: Registro) -> Registro:
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro

    @with_db
    def find_by_id(self, db, id_registro: int) -> Registro | None:
        return db.query(Registro).filter(Registro.id == id_registro).first()

    @with_db
    def find_all_by_usuario_id(self, db, id_usuario: int) -> Registro | None:
        return db.query(Registro).filter(Registro.usuario_id == id_usuario)

    @with_db
    def update(self, db, registro: Registro) -> Registro:
        registro = db.merge(registro)
        db.commit()
        db.refresh(registro)
        return registro