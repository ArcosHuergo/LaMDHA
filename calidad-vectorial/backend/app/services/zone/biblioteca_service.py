from app.models.zone.biblioteca import Biblioteca
from app.repositories.zone.biblioteca_repository import BibliotecaRepository


class BibliotecaService:
    def __init__(self):
        self.biblioteca_repository = BibliotecaRepository()

    def obtener_todas_las_bibliotecas(self) -> list[Biblioteca]:
        """Obtiene todas las bibliotecas.

        Returns:
            Lista de bibliotecas almacenadas.
        """
        return self.biblioteca_repository.find_all()

    def obtener_biblioteca_por_id(self, id: int) -> Biblioteca:
        """Obtiene una biblioteca por su identificador.

        Args:
            id: Identificador de la biblioteca.

        Returns:
            Biblioteca correspondiente al identificador.
        """
        return self.biblioteca_repository.find_by_id(id)

    def obtener_biblioteca_por_nombre(self, nombre: str) -> Biblioteca:
        """Obtiene una biblioteca por su nombre.

        Args:
            nombre: Nombre de la biblioteca.

        Returns:
            Biblioteca correspondiente al nombre indicado.
        """
        return self.biblioteca_repository.find_by_nombre(nombre)
