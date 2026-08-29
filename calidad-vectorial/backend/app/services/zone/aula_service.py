from app.models.zone.aula import Aula
from app.repositories.zone.aula_repository import AulaRepository

class AulaService:
    def __init__(self):
        self.repo = AulaRepository()

    def obtener_todas_las_aulas(self) -> list[Aula]:
        return self.repo.find_all()
    
    def obtener_aula_por_id(self, id: int) -> Aula:
        return self.repo.find_by_id(id)