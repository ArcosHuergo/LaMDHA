from app.models.zone.biblioteca import Biblioteca 
from app.repositories.zone.biblioteca_repository import BibliotecaRepository

class BibliotecaService:
    def __init__(self):
        self.repo = BibliotecaRepository()

    def obtener_todas_las_bibliotecas(self) -> list[Biblioteca]:
        return self.repo.find_all()
    
    def obtener_biblioteca_por_id(self, id: int) -> Biblioteca:
        return self.repo.find_by_id(id)