from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    jwt_secret: str
    jwt_expiration_ms: int 

    # Roboflow (workflow "lamdha" — clasificación de ubicación). Obtener la
    # clave en https://app.roboflow.com/settings/api.
    roboflow_api_key: str 
    roboflow_api_url: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()