import mimetypes
import uuid
from functools import lru_cache
from pathlib import Path

from app.config.settings import settings
from supabase import Client, create_client


class FotoStorageError(Exception):
    """Se produce cuando falla la subida o descarga de una foto."""


@lru_cache
def _get_client() -> Client:
    """Obtiene el cliente de Supabase.

    Returns:
        Cliente de Supabase configurado con la service key.
    """
    return create_client(settings.supabase_url, settings.supabase_service_key)


def guardar_foto(
    contenido: bytes, nombre_original: str, content_type: str | None = None
) -> str:
    """Sube una foto al Supabase Storage.

    Args:
        contenido: Contenido binario de la imagen.
        nombre_original: Nombre original del archivo para obtener su extensión.
        content_type: Tipo MIME de la imagen.

    Returns:
        Ruta del archivo dentro de Supabase.

    Raises:
        FotoStorageError: Si falla la subida al Supabase.
    """
    extension = Path(nombre_original).suffix or ".jpg"
    ruta = f"fotos/{uuid.uuid4().hex}{extension}"
    tipo = content_type or mimetypes.guess_type(ruta)[0] or "image/jpeg"
    try:
        _get_client().storage.from_(settings.supabase_bucket).upload(
            path=ruta,
            file=contenido,
            file_options={"content-type": tipo},
        )
    except Exception as error:
        raise FotoStorageError(f"No se pudo subir la foto: {error}") from error
    return ruta


def descargar_foto(ruta: str) -> bytes:
    """Descarga una foto de Supabase Storage.

    Args:
        ruta: Ruta del archivo dentro de Supabase.

    Returns:
        Contenido binario de la imagen.

    Raises:
        FotoStorageError: Si falla la descarga de Supabase.
    """
    try:
        return _get_client().storage.from_(settings.supabase_bucket).download(ruta)
    except Exception as error:
        raise FotoStorageError(f"No se pudo descargar la foto: {error}") from error