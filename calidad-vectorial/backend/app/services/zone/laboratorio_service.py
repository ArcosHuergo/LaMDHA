from app.models.zone.laboratorio import Laboratorio
from app.repositories.zone.laboratorio_repository import LaboratorioRepository

class LaboratorioService:
    def __init__(self):
        self.laboratorio_repository = LaboratorioRepository()

    def obtener_todos_los_laboratorios(self) -> list[Laboratorio]:
        return self.laboratorio_repository.find_all()
    
    def obtener_laboratorio_por_id(self, id: int) -> Laboratorio:
        return self.laboratorio_repository.find_by_id(id)