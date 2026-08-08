from app.models.sector.zona import Zona
from app.repositories.sector.zona_repository import ZonaRepository

class ZonaService:
    def __init__(self):
        self.repo = ZonaRepository()

    def obtener_todos_las_zonas(self) -> list[Zona]:
        return self.repo.find_all()
    
    def obtener_zona_por_id(self, id: int) -> Zona:
        return self.repo.find_by_id(id)
