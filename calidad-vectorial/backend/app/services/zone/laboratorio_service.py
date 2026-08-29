from app.models.zone.laboratorio import Laboratorio
from app.repositories.zone.laboratorio_repository import LaboratorioRepository

class LaboratorioService:
    def __init__(self):
        self.repo = LaboratorioRepository()

    def obtener_todos_los_laboratorios(self) -> list[Laboratorio]:
        return self.repo.find_all()
    
    def obtener_laboratorio_por_id(self, id: int) -> Laboratorio:
        return self.repo.find_by_id(id)