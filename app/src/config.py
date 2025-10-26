from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    app_name: str = "API Librería"
    app_version: str = "1.0.0"
    database_url: str = "postgresql://admin:admin@db:5432/library_db"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
