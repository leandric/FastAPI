from typing import Optional
from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator("titulo")  # Especifica o campo que o validador irá validar
    def validar_titulo(cls, value):
        palavras = value.split(' ')  # Divide o título em palavras
        if len(palavras) < 3:
            raise ValueError("O título deve conter pelo menos 3 palavras")
        return value.upper()  # Retorna o valor válido

# Lista de cursos
cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=25, horas=56),
    Curso(id=2, titulo='Programação para Iniciantes', aulas=35, horas=156),
    Curso(id=3, titulo='Programação para Avançados', aulas=55, horas=356),
]
