from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.models.security.usuario import Usuario
from app.repositories.log.registro_repository import RegistroRepository
from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.log.hoja_registro_service import HojaRegistroService


class RegistroNoEncontradoError(Exception):
    pass


class RegistroAjenoError(Exception):
    pass


class RegistroService:
    def __init__(self):
        self.registro_repository = RegistroRepository()
        self.hoja_registro_service = HojaRegistroService()

    def registrar_clasificacion(
        self, usuario: Usuario, url_foto: str, prediction: RoboflowPrediction
    ) -> Registro:
        registro = Registro(usuario_id=usuario.id, url_foto=url_foto)
        registro.hoja_registro = [
            HojaRegistro(
                **self.hoja_registro_service.resolver_ubicacion_id(
                    prediccion.clase, prediccion.confianza
                )
            )
            for prediccion in prediction.predicciones
        ]
        return self.registro_repository.insert(registro)

    def obtener_registro_por_id(self, usuario: Usuario, id_registro: int) -> Registro:
        registro = self.registro_repository.find_by_id(id_registro)
        if registro is None:
            raise RegistroNoEncontradoError(f"No existe el registro {id_registro}")
        if registro.usuario_id != usuario.id:
            raise RegistroAjenoError(
                f"El registro {id_registro} pertenece a otro usuario"
            )
        return registro

    def actualizar_prediccion_correcta(
        self, usuario: Usuario, id_registro: int, prediccion_correcta: bool | None
    ) -> Registro:
        registro = self.obtener_registro_por_id(usuario, id_registro)
        registro.prediccion_correcta = prediccion_correcta
        return self.registro_repository.update(registro)

    def obtener_registros_por_usuario(self, usuario: Usuario):
        return self.registro_repository.find_all_by_usuario_id(usuario.id)
