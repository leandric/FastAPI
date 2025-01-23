from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    conteudo: str
    autor_id: int

    class Config:
        orm_mode = True
