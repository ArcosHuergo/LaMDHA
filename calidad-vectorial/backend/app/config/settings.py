from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_port: int = 3306
    db_user: str
    db_password: str
    db_name: str
    JWT_SECRET: str
    JWT_EXPIRATION_MS: int = 30_600_000  # 1 hora por defecto

    # Roboflow (workflow "lamdha" — clasificación de ubicación). Obtener la
    # clave en https://app.roboflow.com/settings/api. Opcional para que el
    # resto de la app siga funcionando si todavía no se configuró.
    roboflow_api_key: str = "UxcfHe8969DfVsTiAuLz"
    roboflow_api_url: str = "https://serverless.roboflow.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()