from app.models.zone.aula import Aula
from app.repositories.zone.aula_repository import AulaRepository

class AulaService:
    def __init__(self):
        self.aula_repository = AulaRepository()

    def obtener_todas_las_aulas(self) -> list[Aula]:
        return self.aula_repository.find_all()
    
    def obtener_aula_por_id(self, id: int) -> Aula:
        return self.aula_repository.find_by_id(id)