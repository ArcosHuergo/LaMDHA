from app.models.zone.pasillo import Pasillo 
from app.repositories.zone.pasillo_repository import PasilloRepository

class PasilloService:
    def __init__(self):
        self.pasillo_repository = PasilloRepository()

    def obtener_todos_los_pasillos(self) -> list[Pasillo]:
        return self.pasillo_repository.find_all()
    
    def obtener_pasillo_por_id(self, id: int) -> Pasillo:
        return self.pasillo_repository.find_by_id(id)