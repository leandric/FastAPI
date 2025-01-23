from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    eh_admin: Optional[bool] = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    pass