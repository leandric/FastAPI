from pytz import timezone
from datetime import datetime, timedelta

from typing import Any, Dict, Optional

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from core.configs import settings
from core.security import verificar_senha
from models.usuario_model import UsuarioModel

from pydantic import EmailStr

oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/usuarios/login")

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique.one_or_none()

        if not usuario:
            return None
        if not verificar_senha(senha, usuario.senha):
            return None
        
        return usuario
    
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(sp) * tempo_vida
    
    payload['type'] = tipo_token
    payload['sub'] = str(sub)
    payload['exp'] = expira
    payload['iat'] = datetime.now(sp)

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def criar_acesso_token(sub: str) -> str:
    return _criar_token('access', timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES), sub)
