from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    API_V1_STR: str = "/api/v1"
    DBBaseModel = declarative_base()
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DBBaseModel: ClassVar = BaseSettings

    class Config:
        case_sensitive = True
        env_file = ".env"

settings: Settings = Settings()

