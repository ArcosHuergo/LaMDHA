from app.models.zone.aula import Aula
from app.repositories.zone.aula_repository import AulaRepository

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class AulaService:
    def __init__(self):
        self.repo = AulaRepository()

    def obtener_todos_las_aulas(self) -> list[Aula]:
        return self.repo.find_all()
    
    def obtener_aula_por_id(self, id: int) -> Aula:
        return self.repo.find_by_id(id)

    

