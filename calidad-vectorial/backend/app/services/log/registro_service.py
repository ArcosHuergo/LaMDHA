from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.models.security.usuario import Usuario
from app.repositories.log.registro_repository import RegistroRepository
from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.log.hoja_registro_service import HojaRegistroService

class RegistroService:
    def __init__(self):
        self.registro_repository = RegistroRepository()
        self.hoja_registro_service = HojaRegistroService()

    def registrar_clasificacion(self, usuario: Usuario, url_foto: str, prediction: RoboflowPrediction) -> Registro:
        registro = Registro(usuario_id=usuario.id, url_foto=url_foto)
        registro.hoja_registro = [
            HojaRegistro(**self.hoja_registro_service.resolver_ubicacion_id(prediccion.clase, prediccion.confianza))
            for prediccion in prediction.predicciones
        ]
        return self.registro_repository.insert(registro)