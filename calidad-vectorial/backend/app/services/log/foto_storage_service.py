import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads/fotos")


def guardar_foto(contenido: bytes, nombre_original: str) -> str:
    """Guarda una foto en el directorio de almacenamiento.

    Args:
        contenido: Contenido binario de la imagen.
        nombre_original: Nombre original del archivo para obtener su extensión.

    Returns:
        Ruta del archivo guardado.
    """
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    extension = Path(nombre_original).suffix or ".jpg"
    nombre_archivo = f"{uuid.uuid4().hex}{extension}"
    ruta = UPLOAD_DIR / nombre_archivo
    ruta.write_bytes(contenido)
    return str(ruta)