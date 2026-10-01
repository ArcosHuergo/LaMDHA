from app.models.sector.zona import Zona
from app.repositories.sector.zona_repository import ZonaRepository


class ZonaService:
    def __init__(self):
        self.zona_repository = ZonaRepository()

    def obtener_todos_las_zonas(self) -> list[Zona]:
        """Obtiene todas las zonas.

        Returns:
            Lista de zonas almacenadas.
        """
        return self.zona_repository.find_all()

    def obtener_zona_por_id(self, id: int) -> Zona:
        """Obtiene una zona por su identificador.

        Args:
            id: Identificador de la zona.

        Returns:
            Zona correspondiente al identificador.
        """
        return self.zona_repository.find_by_id(id)
