from app.models.zone.patio import Patio 
from app.repositories.zone.patio_repository import PatioRepository

class PatioService:
    def __init__(self):
        self.patio_repository = PatioRepository()

    def obtener_todos_los_patios(self) -> list[Patio]:
        return self.patio_repository.find_all()
    
    def obtener_patio_por_id(self, id: int) -> Patio:
        return self.patio_repository.find_by_id(id)

    def obtener_patio_por_nombre(self, nombre: str) -> Patio:
        return self.patio_repository.find_by_nombre(nombre)