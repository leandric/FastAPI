from typing import Any, List, Dict, Optional

from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from fastapi import Header
from fastapi import Depends

from time import sleep

from models import Curso, cursos

def fake_db():
    try:
        print('abrindo conexão com o banco de dados')
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados')
        sleep(1)

app = FastAPI(title='API do Treinamento FastAPI',
              version='0.0.1',
              description='Descrição da API aqui.'
              )



@app.get('/cursos', response_model=List[Curso,], response_description='Cursos retornados')
async def get_cursos(db: Any = Depends(fake_db)):
    """
    Rota para listar todos os cursos.
    
    Retorna:
        dict: Um dicionário contendo todos os cursos disponíveis.
    """
    return cursos

@app.get('/cursos/{curso_id}', response_model=Curso)
async def get_curso(curso_id: int = Path( 
                                        title='ID do curso',
                                        description='Deve ser entre 1 e 7', 
                                        gt=0, lt=8),
                                        db: Any = Depends(fake_db)):
    """
    Rota para obter informações de um curso específico pelo ID.
    
    Parâmetros:
        curso_id (int): ID do curso, deve estar no intervalo entre 1 e 2 (exclusivo).
    
    Retorna:
        dict: As informações do curso solicitado.
        
    Levanta:
        HTTPException: Caso o ID do curso não exista.
    """
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Curso não encontrado')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)) :
    """
    Rota para criar um novo curso.
    
    Parâmetros:
        curso (Curso): Objeto contendo os detalhes do curso a ser criado.
    
    Retorna:
        List[Curso]: A lista de cursos atualizada com o novo curso.
    """
    # Calcula o próximo ID baseado no maior ID existente na lista
    next_id = max([c.id for c in cursos], default=0) + 1
    curso.id = next_id  # Atribui o próximo ID ao curso
    cursos.append(curso)  # Adiciona o curso à lista de cursos
    return cursos  # Retorna a lista de cursos atualizada


@app.put('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    """
    Rota para atualizar informações de um curso existente.
    
    Parâmetros:
        curso_id (int): ID do curso a ser atualizado.
        curso (Curso): Objeto contendo as novas informações do curso.
    
    Retorna:
        Curso: As informações atualizadas do curso.
        
    Levanta:
        HTTPException: Caso o ID do curso não exista.
    """
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID de curso não existe')

@app.delete('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    """
    Rota para excluir um curso pelo ID.
    
    Parâmetros:
        curso_id (int): ID do curso a ser excluído.
    
    Retorna:
        dict: As informações do curso excluído.
        
    Levanta:
        HTTPException: Caso o ID do curso não exista.
    """
    if curso_id in cursos:
        return cursos.pop(curso_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não existe')

@app.get('/calculadora', status_code=status.HTTP_202_ACCEPTED)
async def calculadora(a: int = Query(default=6, gt=5),
                       b: int = Query(default=101, gt=10),
                       x_geek: str = Header(default=None),
                       c: Optional[int] = 0):
    """
    Rota para realizar a soma de até três números.

    Parâmetros:
        a (int): Primeiro número, valor mínimo 6 (padrão: 6).
        b (int): Segundo número, valor mínimo 11 (padrão: 101).
        x_geek (str): Valor opcional de um cabeçalho chamado 'x-geek'.
        c (Optional[int]): Terceiro número, opcional, valor padrão 0.

    Retorna:
        dict: O resultado da soma dos valores fornecidos e o valor do cabeçalho 'x-geek', caso presente.

    Comportamento:
        - O valor do cabeçalho 'x-geek' é exibido no console através do print.
    """
    print({'header': x_geek})
    return {'soma': a + b + c}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='debug', reload=True)
