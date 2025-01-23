from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class ArtigoModel(settings.DBBaseModel):
    __tablename__ = "artigos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    conteudo = Column(String)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))

    autor = relationship("UsuarioModel", back_populates="artigos", lazy="joined")
