from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    jwt_secret: str
    jwt_expiration_ms: int

    roboflow_api_key: str
    roboflow_api_url: str
    workspace_name: str
    workflow_id: str

    supabase_url: str
    supabase_service_key: str
    supabase_bucket: str = "fotos"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()