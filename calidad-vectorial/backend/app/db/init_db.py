from app.models import Aula, Biblioteca, Laboratorio, Pasillo, Patio, Usuario, Zona
from app.services.security.usuario_service import UsuarioService
from sqlalchemy.orm import Session

AULAS_SEED = [
    {
        "nombre": "Aula-PB-Violeta-3",
        "referencia": "A3",
        "color_zona": "Violeta",
        "descripcion": "Aula ubicada en Planta Baja, sector Violeta, destinada al dictado de clases teóricas y prácticas de distintos talleres.",
    },
    {
        "nombre": "Aula-EP1-Blanco-1",
        "referencia": "A1",
        "color_zona": "Blanco",
        "descripcion": "Aula numero 1 ubicada en el Entre Piso 1, sector Blanco, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-EP1-Blanco-3",
        "referencia": "A3",
        "color_zona": "Blanco",
        "descripcion": "Aula numero 3 ubicada en el Entre Piso 1 con vista al patio, sector Blanco, destinada al dictado de clases teóricas con vista al cancha de Educacion Fisica.",
    },
    {
        "nombre": "Aula-EP1-Naranja-1",
        "referencia": "A1",
        "color_zona": "Naranja",
        "descripcion": "Aula numero 1 ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-EP1-Naranja-2",
        "referencia": "A2",
        "color_zona": "Naranja",
        "descripcion": "Aula numero 2 ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-EP1-Naranja-3",
        "referencia": "A3",
        "color_zona": "Naranja",
        "descripcion": "Aula numero 3 ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases teóricas y cuenta con un equipo audiovisual.",
    },
    {
        "nombre": "Aula-EP1-Naranja-4",
        "referencia": "A4",
        "color_zona": "Naranja",
        "descripcion": "Aula ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases de dibujo técnico.",
    },
    {
        "nombre": "Aula-EP1-Naranja-5",
        "referencia": "A5",
        "color_zona": "Naranja",
        "descripcion": "Aula ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases de dibujo técnico.",
    },
    {
        "nombre": "Aula-EP1-Naranja-6",
        "referencia": "A6",
        "color_zona": "Naranja",
        "descripcion": "Aula ubicada en el Entre Piso 1, sector Naranja, destinada al dictado de clases teóricas con vista a la escalera y biblioteca, cuento con equipo audiovisual.",
    },
    {
        "nombre": "Aula-P1-Amarillo-2",
        "referencia": "A2",
        "color_zona": "Amarillo",
        "descripcion": "Aula ubicada en el Piso 1, sector Amarillo, destinada al dictado de clases teóricas al lado del baño de damas y cuenta con equipo audio visual.",
    },
    {
        "nombre": "Aula-P1-Gris-4",
        "referencia": "A4",
        "color_zona": "Gris",
        "descripcion": "Aula ubicada en el Piso 1 en frente del mástil, sector Gris, destinada al dictado de clases teóricas con vista al mastil y al lado de sala de ingles.",
    },
    {
        "nombre": "Aula-P2-Blanco-4",
        "referencia": "A4",
        "color_zona": "Blanco",
        "descripcion": "Aula ubicada en el Piso 2, sector Blanco, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-P2-Blanco-5",
        "referencia": "A5",
        "color_zona": "Blanco",
        "descripcion": "Aula ubicada en el Piso 2, sector Blanco, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-P2-Blanco-6",
        "referencia": "A6",
        "color_zona": "Blanco",
        "descripcion": "Aula ubicada en el Piso 2, sector Blanco, destinada al dictado de clases teóricas.",
    },
    {
        "nombre": "Aula-P2-Blanco-7",
        "referencia": "A7",
        "color_zona": "Blanco",
        "descripcion": "Aula ubicada en el Piso 2, sector Blanco, destinada al dictado de clases teóricas.",
    },
    { 
        "nombre": "Aula-P2-Rojo-2",
        "referencia": "A2",
        "color_zona": "Rojo",
        "descripcion": "Aula ubicada en el Piso 2, sector Rojo, destinada al dictado de clases teóricas al lado del aula de musica.",
    },
    {
        "nombre": "Aula-P2-Rojo-7",
        "referencia": "A7",
        "color_zona": "Rojo",
        "descripcion": "Aula ubicada en el Piso 2 al lado del salón de actos, sector Rojo, destinada al dictado de clases teóricas.",
    },
    {  
        "nombre": "Aula-P2-Rojo-8",
        "referencia": "A8",
        "color_zona": "Rojo",
        "descripcion": "Aula ubicada en el Piso 2, sector Rojo, destinada al dictado de clases teóricas.",
    },
    {  
        "nombre": "Aula-P2-Rojo-9",
        "referencia": "A9",
        "color_zona": "Rojo",
        "descripcion": "Aula ubicada en el Piso 2, sector Rojo, destinada al dictado de clases teóricas.",
    },
]

LABORATORIOS_SEED = [
    {
        "nombre": "Laboratorio-PB-Violeta-2",
        "referencia": "L2",
        "color_zona": "Violeta",
        "descripcion": "Laboratorio ubicado en Planta baja, sector Violeta, destinado al desarrollo de actividades prácticas de las especialidades de Electrónica.",
    },
    {
        "nombre": "Laboratorio-PB-Violeta-4",
        "referencia": "L4",
        "color_zona": "Violeta",
        "descripcion": "Laboratorio de electrónica ubicado en Planta baja, sector Violeta, destinado al desarrollo de actividades prácticas de la especialidad de Electrónica.",
    },
    {
        "nombre": "Laboratorio-PB-Violeta-5",
        "referencia": "L5",
        "color_zona": "Violeta",
        "descripcion": "Laboratorio de química ubicado en Planta baja, sector Violeta, destinado al desarrollo de actividades prácticas de la especialidad de Química.",
    },
    {
        "nombre": "Laboratorio-PB-Violeta-7",
        "referencia": "L7",
        "color_zona": "Violeta",
        "descripcion": "Laboratorio de electrónica ubicado en Planta baja, sector Violeta, destinado al desarrollo de actividades prácticas de la especialidad de Electrónica y Energías Renovables.",
    },
    {  
        "nombre": "Laboratorio-EPB-Verde-3",
        "referencia": "L3",
        "color_zona": "Verde",
        "descripcion": "Laboratorio ubicado en Entre Planta Baja, sector Verde, destinado al desarrollo de actividades prácticas y teóricas de la especialidad de Química.",
    },
    { 
        "nombre": "Laboratorio-EPB-Verde-4",
        "referencia": "L4",
        "color_zona": "Verde",
        "descripcion": "Laboratorio ubicado en Entre Planta Baja, sector Verde, destinado al desarrollo de actividades prácticas y teóricas de la especialidad de Construcciones.",
    },
    {
        "nombre": "Laboratorio-EPB-Azul-6",
        "referencia": "L6",
        "color_zona": "Azul",
        "descripcion": "Laboratorio ubicado en Entre Planta Baja, sector Azul, destinado al desarrollo de actividades prácticas y teóricas de las especialidades de Química y Física.",
    },
    {
        "nombre": "Laboratorio-P1-Gris-1",
        "referencia": "L1",
        "color_zona": "Gris",
        "descripcion": "Laboratorio ubicado en Piso 1, sector Gris, destinado al desarrollo de actividades prácticas y teóricas de las especialidades de Computación y Mecánica.",
    },
    {
        "nombre": "Laboratorio-P2-Rojo-10",
        "referencia": "A10",
        "color_zona": "Rojo",
        "descripcion": "Laboratorio de computación ubicado en Piso 2, sector Rojo, destinado al desarrollo de actividades prácticas de la especialidad de Computación.",
    },
]

PATIOS_SEED = [
    {  
        "nombre": "Patio-PB-Turquesa-1",
        "referencia": "P1",
        "color_zona": "Turquesa",
        "descripcion": "Patio ubicado en Planta Baja, sector Turquesa, destinado a la clases de Educación Física y actividades exteriores.",
    },
    {  
        "nombre": "Patio-PB-Turquesa-2",
        "referencia": "P2",
        "color_zona": "Turquesa",
        "descripcion": "Patio ubicado en Planta Baja, sector Turquesa, destinado a la clases de Educación Física y actividades exteriores.",
    },
    { 
        "nombre": "Patio-P1-Amarillo-3",
        "referencia": "P3",
        "color_zona": "Amarillo",
        "descripcion": "Patio ubicado en el Piso 1, sector Amarillo, destinado al uso del comedor.",
    },
    { 
        "nombre": "Patio-P2-Rojo-6",
        "referencia": "P6",
        "color_zona": "Rojo",
        "descripcion": "Salon de actos ubicado en el Piso 2, sector Rojo, destinado a eventos especiales.",
    },
]

PASILLOS_SEED = [
    {
        "nombre": "Pasillo-PB-Azul",
        "color_zona": "Azul",
        "descripcion": "Pasillo ubicado en Planta Baja, sector Azul.",
    },
    {
        "nombre": "Pasillo-PB-Violeta",
        "color_zona": "Violeta",
        "descripcion": "Pasillo ubicado en Planta Baja, sector Violeta.",
    },
    {  
        "nombre": "Pasillo-PB-Entrada",
        "color_zona": "Entrada",
        "descripcion": "Pasillo ubicado en Planta Baja, en la entrada de la institución.",
    },
    
    { 
        "nombre": "Pasillo-EP1-Naranja",
        "color_zona": "Naranja",
        "descripcion": "Pasillo ubicado en el Entre Piso 1, sector Naranja.",
    },
    {
        "nombre": "Pasillo-P1-Amarillo",
        "color_zona": "Amarillo",
        "descripcion": "Pasillo ubicado en Piso 1, sector Amarillo.",
    },
    {   "nombre": "Pasillo-P1-Mastil",
        "color_zona": "Mastil",
        "descripcion": "Pasillo ubicado en Piso 1, junto al mástil.",
    },
    {  
        "nombre": "Pasillo-P2-Rojo",
        "color_zona": "Rojo",
        "descripcion": "Pasillo ubicado en Piso 2, sector Rojo.",
    },
]

BIBLIOTECA_SEED = [
    {
        "nombre": "Biblioteca-EP1-Biblioteca",
        "referencia": "Biblioteca",
        "color_zona": "Biblioteca",
        "descripcion": "Biblioteca ubicada en Entre Piso 1.",
    },
]


def _obtener_o_crear_zona(
    db: Session,
    cache: dict[str, Zona],
    color: str,
) -> Zona:
    """Obtiene una zona existente o crea una nueva.

    Args:
        db: Sesión activa de SQLAlchemy.
        cache: Caché de zonas ya consultadas o creadas.
        color: Color identificador de la zona.

    Returns:
        Zona existente o recién creada.
    """
    if color not in cache:
        zona = db.query(Zona).filter(Zona.color == color).first()

        if zona is None:
            zona = Zona(color=color)
            db.add(zona)
            db.flush()

        cache[color] = zona

    return cache[color]


def _seed_aulas(db: Session, cache: dict[str, Zona]) -> None:
    """Carga las aulas iniciales si todavía no existen."""
    for data in AULAS_SEED:
        if db.query(Aula).filter(Aula.nombre == data["nombre"]).first():
            continue

        zona = _obtener_o_crear_zona(db, cache, data["color_zona"])
        zona.aula.append(
            Aula(
                nombre=data["nombre"],
                referencia=data["referencia"],
                descripcion=data["descripcion"],
            )
        )


def _seed_laboratorios(db: Session, cache: dict[str, Zona]) -> None:
    """Carga los laboratorios iniciales si todavía no existen."""
    for data in LABORATORIOS_SEED:
        if (
            db.query(Laboratorio)
            .filter(Laboratorio.nombre == data["nombre"])
            .first()
        ):
            continue

        zona = _obtener_o_crear_zona(db, cache, data["color_zona"])
        zona.laboratorio.append(
            Laboratorio(
                nombre=data["nombre"],
                referencia=data["referencia"],
                descripcion=data["descripcion"],
            )
        )


def _seed_pasillos(db: Session, cache: dict[str, Zona]) -> None:
    """Carga los pasillos iniciales si todavía no existen."""
    for data in PASILLOS_SEED:
        if db.query(Pasillo).filter(Pasillo.nombre == data["nombre"]).first():
            continue

        zona = _obtener_o_crear_zona(db, cache, data["color_zona"])
        zona.pasillo = Pasillo(
            nombre=data["nombre"],
            descripcion=data["descripcion"],
        )


def _seed_patios(db: Session, cache: dict[str, Zona]) -> None:
    """Carga los patios iniciales si todavía no existen."""
    for data in PATIOS_SEED:
        if db.query(Patio).filter(Patio.nombre == data["nombre"]).first():
            continue

        zona = _obtener_o_crear_zona(db, cache, data["color_zona"])
        zona.patio.append(
            Patio(
                nombre=data["nombre"],
                referencia=data["referencia"],
                descripcion=data["descripcion"],
            )
        )


def _seed_bibliotecas(db: Session, cache: dict[str, Zona]) -> None:
    """Carga las bibliotecas iniciales si todavía no existen."""
    for data in BIBLIOTECA_SEED:
        if db.query(Biblioteca).filter(Biblioteca.nombre == data["nombre"]).first():
            continue

        zona = _obtener_o_crear_zona(db, cache, data["color_zona"])
        zona.biblioteca = Biblioteca(
            nombre=data["nombre"],
            referencia=data["referencia"],
            descripcion=data["descripcion"],
        )


def init_db(db: Session) -> None:
    """Inicializa los datos base de la aplicación.

    Crea un usuario de prueba y carga las zonas, aulas, laboratorios,
    pasillos, patios y bibliotecas definidas en los datos iniciales.
    Los registros existentes no se duplican.

    Args:
        db: Sesión activa de SQLAlchemy.
    """
    usuario = db.query(Usuario).filter(Usuario.username == "test@test").first()

    if usuario is None:
        usuario = Usuario(
            username="test@test",
            password=UsuarioService.hash_password("test123"),
            nickname="Usuario Test",
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

    zonas_cache: dict[str, Zona] = {}

    _seed_aulas(db, zonas_cache)
    _seed_laboratorios(db, zonas_cache)
    _seed_pasillos(db, zonas_cache)
    _seed_patios(db, zonas_cache)
    _seed_bibliotecas(db, zonas_cache)

    db.commit()
    print("Seed ejecutado correctamente.")
