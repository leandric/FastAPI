from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship("ArtigoModel", back_populates="autor", cascade="all, delete-orphan", uselist=True, lazy='joined')
    