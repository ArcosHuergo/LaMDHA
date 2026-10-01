from app.models.zone.patio import Patio
from app.repositories.zone.patio_repository import PatioRepository


class PatioService:
    def __init__(self):
        self.patio_repository = PatioRepository()

    def obtener_todos_los_patios(self) -> list[Patio]:
        """Obtiene todos los patios.

        Returns:
            Lista de patios almacenados.
        """
        return self.patio_repository.find_all()

    def obtener_patio_por_id(self, id: int) -> Patio:
        """Obtiene un patio por su identificador.

        Args:
            id: Identificador del patio.

        Returns:
            Patio correspondiente al identificador.
        """
        return self.patio_repository.find_by_id(id)

    def obtener_patio_por_nombre(self, nombre: str) -> Patio:
        """Obtiene un patio por su nombre.

        Args:
            nombre: Nombre del patio.

        Returns:
            Patio correspondiente al nombre indicado.
        """
        return self.patio_repository.find_by_nombre(nombre)
