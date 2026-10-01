from app.models.zone.pasillo import Pasillo
from app.repositories.zone.pasillo_repository import PasilloRepository


class PasilloService:
    def __init__(self):
        self.pasillo_repository = PasilloRepository()

    def obtener_todos_los_pasillos(self) -> list[Pasillo]:
        """Obtiene todos los pasillos.

        Returns:
            Lista de pasillos almacenados.
        """
        return self.pasillo_repository.find_all()

    def obtener_pasillo_por_nombre(self, nombre: str) -> Pasillo:
        """Obtiene un pasillo por su nombre.

        Args:
            nombre: Nombre del pasillo.

        Returns:
            Pasillo correspondiente al nombre indicado.
        """
        return self.pasillo_repository.find_by_nombre(nombre)
