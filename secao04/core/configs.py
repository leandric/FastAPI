from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Carregar o arquivo .env
load_dotenv()

class Settings(BaseSettings):
    """
    Configurações gerais
    """
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    DB_URL: str = os.getenv("DB_URL", "postgresql+asyncpg://default_user:default_password@localhost:5432/default_db")
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()


