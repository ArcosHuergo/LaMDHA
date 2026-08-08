# app/db/init_db.py
from sqlalchemy.orm import Session
from app.models import Usuario, Zona, Pasillo, Aula, Patio
from app.services.security.usuario_service import UsuarioService


def init_db(db: Session) -> None:

    # --- Usuario de prueba ---
    usuario = db.query(Usuario).filter(Usuario.username == "test@test.com").first()
    if not usuario:
        usuario = Usuario(
            username = "test@test.com",
            password = UsuarioService.hash_password("test123"),
            nickname = "Usuario Test",
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

    # --- Zona ---
    zona = db.query(Zona).filter(Zona.color == "Verde").first()
    if not zona:
        zona = Zona(
            color = "Verde",
        )
        db.add(zona)
        db.flush()

    # --- Pasillo, Aula y Patio ---
    if not db.query(Pasillo).filter(Pasillo.nombre == "Pasillo 1").first():
        zona.pasillo = Pasillo(nombre="Pasillo 1", descripcion="Pasillo test")

    if not db.query(Aula).filter(Aula.nombre == "Aula 101").first():
        zona.aulas.append(Aula(nombre="Aula 101", referencia="A1", descripcion="Patio test"))

    if not db.query(Patio).filter(Patio.nombre == "Patio 1").first():
        zona.patio = Patio(nombre="Patio 1", referencia="P1", descripcion="Aula test")

    db.commit()
    print("Seed ejecutado correctamente.")