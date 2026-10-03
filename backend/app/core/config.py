"""
Configuración central. Lee variables de entorno desde .env
para no dejar llaves ni secretos escritos en el código.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CodeSentinel"
    environment: str = "development"

    # Base de datos (SQLite en desarrollo; se puede apuntar a PostgreSQL/SQL Server luego)
    database_url: str = "sqlite:///./codesentinel.db"

    # Proveedor de IA: "gemini" o "groq" (ver docs/ENTORNO.md)
    ai_provider: str = "gemini"
    ai_api_key: str = ""

    # Autenticación
    secret_key: str = "cambiar-esta-clave-en-produccion"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
