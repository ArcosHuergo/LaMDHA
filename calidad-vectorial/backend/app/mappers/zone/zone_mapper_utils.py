class ZoneMapperUtills:
    @staticmethod
    def extraer_data_zone(nombre_zone: str):
        data = nombre_zone.split("-")
        return {"tipo": data[0], "zona_color": data[2]}
