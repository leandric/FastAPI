from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine  

from core.configs import settings

# Criação do engine para SQLite
# Importante: Use o driver `aiosqlite` para suporte assíncrono no SQLite
engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL, 
    echo=True, 
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

# Configuração da sessão assíncrona
Session: AsyncSession = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False, 
    autoflush=False
)
