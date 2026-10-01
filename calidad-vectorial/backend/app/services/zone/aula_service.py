from app.models.zone.aula import Aula
from app.repositories.zone.aula_repository import AulaRepository


class AulaService:
    def __init__(self):
        self.aula_repository = AulaRepository()

    def obtener_todas_las_aulas(self) -> list[Aula]:
        """Obtiene todas las aulas.

        Returns:
            Lista de aulas almacenadas.
        """
        return self.aula_repository.find_all()

    def obtener_aula_por_id(self, id: int) -> Aula:
        """Obtiene un aula por su identificador.

        Args:
            id: Identificador del aula.

        Returns:
            Aula correspondiente al identificador.
        """
        return self.aula_repository.find_by_id(id)

    def obtener_aula_por_nombre(self, nombre: str) -> Aula:
        """Obtiene un aula por su nombre.

        Args:
            nombre: Nombre del aula.

        Returns:
            Aula correspondiente al nombre indicado.
        """
        return self.aula_repository.find_by_nombre(nombre)
