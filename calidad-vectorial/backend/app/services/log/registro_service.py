from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.models.security.usuario import Usuario
from app.repositories.log.registro_repository import RegistroRepository
from app.schemas.vision.roboflow_prediction import RoboflowPrediction
from app.services.log.hoja_registro_service import HojaRegistroService


class RegistroNoEncontradoError(Exception):
    """Se produce cuando no se encuentra un registro."""


class RegistroAjenoError(Exception):
    """Se produce cuando un registro pertenece a otro usuario."""


class RegistroService:
    def __init__(self):
        self.registro_repository = RegistroRepository()
        self.hoja_registro_service = HojaRegistroService()

    def registrar_clasificacion(
        self, usuario: Usuario, url_foto: str, prediction: RoboflowPrediction
    ) -> Registro:
        """Registra una clasificación asociada a un usuario.

        Args:
            usuario: Usuario al que pertenece la clasificación.
            url_foto: Ruta de la foto asociada al registro.
            prediction: Predicción obtenida de la clasificación.

        Returns:
            Registro creado con las ubicaciones identificadas.
        """
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
        """Obtiene un registro verificando que pertenezca al usuario.

        Args:
            usuario: Usuario propietario del registro.
            id_registro: Identificador del registro.

        Returns:
            Registro solicitado.

        Raises:
            RegistroNoEncontradoError: Si el registro no existe.
            RegistroAjenoError: Si el registro pertenece a otro usuario.
        """
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
        """Actualiza la valoración de una predicción de un registro.

        Args:
            usuario: Usuario propietario del registro.
            id_registro: Identificador del registro.
            prediccion_correcta: Indica si la predicción fue correcta.

        Returns:
            Registro actualizado.

        Raises:
            RegistroNoEncontradoError: Si el registro no existe.
            RegistroAjenoError: Si el registro pertenece a otro usuario.
        """
        registro = self.obtener_registro_por_id(usuario, id_registro)
        registro.prediccion_correcta = prediccion_correcta
        return self.registro_repository.update(registro)

    def obtener_registros_por_usuario(self, usuario: Usuario):
        """Obtiene todos los registros asociados a un usuario.

        Args:
            usuario: Usuario cuyos registros se desean obtener.

        Returns:
            Lista de registros pertenecientes al usuario.
        """
        return self.registro_repository.find_all_by_usuario_id(usuario.id)
