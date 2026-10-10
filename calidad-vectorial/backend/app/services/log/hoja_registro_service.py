from app.models.log.hoja_registro import HojaRegistro
from app.models.log.registro import Registro
from app.repositories.zone.aula_repository import AulaRepository
from app.repositories.zone.biblioteca_repository import BibliotecaRepository
from app.repositories.zone.laboratorio_repository import LaboratorioRepository
from app.repositories.zone.pasillo_repository import PasilloRepository
from app.repositories.zone.patio_repository import PatioRepository


class HojaRegistroService:
    def __init__(self):
        self.aula_repository = AulaRepository()
        self.laboratorio_repository = LaboratorioRepository()
        self.pasillo_repository = PasilloRepository()
        self.patio_repository = PatioRepository()
        self.biblioteca_repository = BibliotecaRepository()

        self.resolvers = {
            "Aula": (self.aula_repository, "aula_id"),
            "Laboratorio": (self.laboratorio_repository, "labo_id"),
            "Pasillo": (self.pasillo_repository, "pasillo_id"),
            "Patio": (self.patio_repository, "patio_id"),
            "Biblioteca": (self.biblioteca_repository, "biblioteca_id"),
        }

    def resolver_ubicacion_id(self, clase: str, confianza: float) -> dict:
        """Resuelve el identificador de una ubicación a partir de su clase.

        Busca la entidad correspondiente al tipo de sector y asigna su
        identificador junto con el nivel de confianza de la predicción.

        Args:
            clase: Clase de ubicación obtenida de la predicción.
            confianza: Nivel de confianza de la predicción.

        Returns:
            Diccionario con el identificador de la ubicación y su confianza.
        """
        ubicacion = {
            "aula_id": None,
            "labo_id": None,
            "pasillo_id": None,
            "patio_id": None,
            "biblioteca_id": None,
        }

        tipo_sector = clase.split("-")[0]
        resolver = self.resolvers.get(tipo_sector)
        if resolver is None:
            ubicacion["confianza"] = 0
            return ubicacion

        repository, campo_id_sector = resolver
        entidad = repository.find_by_nombre(clase)
        if entidad is None:
            ubicacion["confianza"] = 0
            return ubicacion

        ubicacion[campo_id_sector] = entidad.id
        ubicacion["confianza"] = confianza
        return ubicacion

    def obtener_hoja_principal(self, registro: Registro) -> HojaRegistro | None:
        """Obtiene la hoja de registro con mayor confianza de un registro.

        Args:
            registro: Registro del que se desea obtener la hoja principal.

        Returns:
            Hoja con mayor confianza, o None si el registro no tiene hojas o
            la mejor no pudo resolverse a una ubicación (confianza 0).
        """
        if not registro.hoja_registro:
            return None

        hoja_principal = max(registro.hoja_registro, key=lambda hoja: hoja.confianza)
        if hoja_principal.confianza <= 0:
            return None
        return hoja_principal
