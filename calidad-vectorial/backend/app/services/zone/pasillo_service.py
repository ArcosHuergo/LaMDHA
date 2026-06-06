from app.models.zone.pasillo import Pasillo 
from app.repositories.zone.pasillo_repository import PasilloRepository

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class PasilloService:
    def __init__(self):
        self.repo = PasilloRepository()

    def obtener_todos_los_pasillos(self) -> list[Pasillo]:
        return self.repo.find_all()
    
    def obtener_pasillo_por_id(self, id: int) -> Pasillo:
        return self.repo.find_by_id(id)
