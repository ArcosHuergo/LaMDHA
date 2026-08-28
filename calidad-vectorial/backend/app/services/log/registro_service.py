from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.models.security.usuario import Usuario
from app.repositories.log.registro_repository import RegistroRepository
from app.schemas.vision.roboflow_prediction import RoboflowPrediction

class RegistroService:
    def __init__(self):
        self.repo = RegistroRepository()

    def registrar_clasificacion(self, usuario: Usuario, url_foto: str, prediction: RoboflowPrediction) -> Registro:
        registro = Registro(usuario_id=usuario.id, url_foto=url_foto)
        registro.hoja_registro = [
            HojaRegistro(confianza=p.confianza)
            for p in prediction.predicciones
        ]
        return self.repo.insert(registro)