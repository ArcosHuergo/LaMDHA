from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_port: int = 3306
    db_user: str
    db_password: str
    db_name: str
    JWT_SECRET: str
    JWT_EXPIRATION_MS: int = 30_600_000  # 1 hora por defecto


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()