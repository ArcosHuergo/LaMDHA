from app.models.zone.laboratorio import Laboratorio
from app.repositories.zone.laboratorio_repository import LaboratorioRepository


class LaboratorioService:
    def __init__(self):
        self.laboratorio_repository = LaboratorioRepository()

    def obtener_todos_los_laboratorios(self) -> list[Laboratorio]:
        """Obtiene todos los laboratorios.

        Returns:
            Lista de laboratorios almacenados.
        """
        return self.laboratorio_repository.find_all()

    def obtener_laboratorio_por_id(self, id: int) -> Laboratorio:
        """Obtiene un laboratorio por su identificador.

        Args:
            id: Identificador del laboratorio.

        Returns:
            Laboratorio correspondiente al identificador.
        """
        return self.laboratorio_repository.find_by_id(id)

    def obtener_laboratorio_por_nombre(self, nombre: str) -> Laboratorio:
        """Obtiene un laboratorio por su nombre.

        Args:
            nombre: Nombre del laboratorio.

        Returns:
            Laboratorio correspondiente al nombre indicado.
        """
        return self.laboratorio_repository.find_by_nombre(nombre)
