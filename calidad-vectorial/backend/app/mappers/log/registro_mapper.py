from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.schemas.log.registro_completo import RegistroCompletoSchema
from app.schemas.log.registro_feedback import RegistroFeedbackSchema


class RegistroMapper:
    """Mapea entidades de registro a sus esquemas de respuesta."""

    @staticmethod
    def to_schema(entity: Registro) -> RegistroFeedbackSchema:
        """Convierte un registro en un esquema de feedback.

        Args:
            entity: entidad de registro que se desea convertir.

        Returns:
            Esquema de feedback con el resultado de la predicción.
        """
        return RegistroFeedbackSchema(prediccion_correcta=entity.prediccion_correcta)

    @staticmethod
    def resolver_ubicacion(hoja_principal: HojaRegistro | None) -> dict:
        """Obtiene los datos de la ubicación identificada en una hoja.

        Args:
            hoja_principal: Hoja de registro de mayor confianza.

        Returns:
            Diccionario con sector, piso, tipo, referencia y confianza en
            porcentaje. Los valores son None si no hay ubicación identificada.
        """
        ubicacion = {
            "sector": None,
            "piso": None,
            "tipo": None,
            "referencia": None,
            "confianza": None,
        }
        if hoja_principal is None:
            return ubicacion

        entidad_encontrada = next(
            (
                valor
                for valor in vars(hoja_principal).values()
                if hasattr(valor, "zona")
            ),
            None,
        )
        if entidad_encontrada is None:
            return ubicacion

        ubicacion.update(
            sector=entidad_encontrada.zona.color,
            piso=entidad_encontrada.nombre.split("-")[1],
            tipo=type(entidad_encontrada).__name__,
            referencia=getattr(entidad_encontrada, "referencia", None),
            confianza=round(float(hoja_principal.confianza) * 100, 2),
        )
        return ubicacion

    @staticmethod
    def to_schema_completo(
        entity: Registro, hoja_principal: HojaRegistro | None
    ) -> RegistroCompletoSchema:
        """Convierte un registro en un esquema con información completa.

        Args:
            entity: entidad de registro que se desea convertir.
            hoja_principal: Hoja de registro de mayor confianza.

        Returns:
            Esquema con la información completa del registro.
        """
        return RegistroCompletoSchema(
            id=entity.id,
            prediccion_correcta=entity.prediccion_correcta,
            fecha_creacion=entity.fecha_creacion,
            **RegistroMapper.resolver_ubicacion(hoja_principal),
        )

    @staticmethod
    def to_schema_completo_list(
        entities: list[tuple[Registro, HojaRegistro | None]],
    ) -> list[RegistroCompletoSchema]:
        """Convierte una lista de registros en esquemas completos.

        Args:
            entities: Lista de pares con cada registro y su hoja principal.

        Returns:
            Lista de esquemas con la información completa de cada registro.
        """
        return [
            RegistroMapper.to_schema_completo(entity, hoja_principal)
            for entity, hoja_principal in entities
        ]
