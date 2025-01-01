# Documentação da API do Treinamento FastAPI

## Objetivo
Esta aplicação foi criada como parte de um treinamento para entender o funcionamento do **FastAPI**. O código implementa uma API para gerenciamento de cursos, abordando conceitos como validações, dependências, manipulação de dados em memória e uso de ferramentas do framework.

---

## Estrutura do Código
### Organização Principal
O código é composto por:
1. **Função de simulação de banco de dados (`fake_db`)**:
   - Simula a abertura e o fechamento de uma conexão com um banco de dados.
   - Utiliza o recurso de dependências do FastAPI para ser executada automaticamente antes e depois das rotas.

2. **Modelo de Dados (`Curso`)**:
   - Define a estrutura de um curso usando `Pydantic`, garantindo validações de tipo e regras específicas, como títulos com pelo menos três palavras.

3. **Lista de Cursos (`cursos`)**:
   - Representa um banco de dados em memória para armazenar os cursos durante a execução da aplicação.

4. **Rotas HTTP**:
   - Endpoints implementados para manipular os dados em memória.

---

## Funcionamento Lógico

### 1. **Modelo `Curso`**
O modelo `Curso` é usado para definir e validar os cursos armazenados. Sua estrutura é:
- **`id`**: (Opcional) Identificador único do curso. Gerado automaticamente ao criar um novo curso.
- **`titulo`**: O título do curso. Validado para garantir que tenha ao menos três palavras.
- **`aulas` e `horas`**: Quantidade de aulas e horas do curso, ambos do tipo `int`.

#### Validação de `titulo`
```python
@field_validator("titulo")
def validar_titulo(cls, value):
    palavras = value.split(' ')
    if len(palavras) < 3:
        raise ValueError("O título deve conter pelo menos 3 palavras")
    return value.upper()
```
A validação garante que:
- O título tenha no mínimo três palavras.
- Seja retornado em letras maiúsculas.

---

### 2. **Função `fake_db`**
Simula o ciclo de vida de uma conexão com o banco de dados:
```python
def fake_db():
    try:
        print('Abrindo conexão com o banco de dados')
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados')
        sleep(1)
```
- Executada automaticamente antes de cada rota por meio de `Depends`.
- Demonstra a utilização de recursos externos (como um banco de dados).

---

### 3. **Rotas e Lógica**
#### **Listar Todos os Cursos**
```python
@app.get('/cursos', response_model=List[Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos
```
- **Responsabilidade**: Retorna todos os cursos disponíveis.
- **Lógica**: A lista `cursos` é retornada diretamente. Não há interação com banco de dados ou persistência.

---

#### **Obter Curso por ID**
```python
@app.get('/cursos/{curso_id}', response_model=Curso)
async def get_curso(curso_id: int = Path(gt=0, lt=8), db: Any = Depends(fake_db)):
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
```
- **Responsabilidade**: Retorna os detalhes de um curso específico.
- **Lógica**:
  1. Valida que o `curso_id` está no intervalo permitido.
  2. Busca o curso na lista `cursos` usando o ID como chave.
  3. Caso o ID não exista, uma exceção `HTTPException` é levantada.

---

#### **Criar Curso**
```python
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id = max([c.id for c in cursos], default=0) + 1
    curso.id = next_id
    cursos.append(curso)
    return cursos
```
- **Responsabilidade**: Adiciona um novo curso.
- **Lógica**:
  1. Calcula o próximo ID com base no maior ID existente na lista.
  2. Atualiza o ID do curso criado e adiciona-o à lista `cursos`.

---

#### **Atualizar Curso**
```python
@app.put('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID de curso não existe')
```
- **Responsabilidade**: Atualiza informações de um curso existente.
- **Lógica**:
  1. Verifica se o curso existe na lista.
  2. Atualiza as informações com o novo objeto recebido.
  3. Remove o campo `id` do curso, caso exista.

---

#### **Excluir Curso**
```python
@app.delete('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        return cursos.pop(curso_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não existe')
```
- **Responsabilidade**: Remove um curso pelo ID.
- **Lógica**:
  1. Busca o curso na lista.
  2. Remove e retorna as informações do curso.
  3. Caso o ID não exista, levanta uma exceção.

---

#### **Calculadora**
```python
@app.get('/calculadora', status_code=status.HTTP_202_ACCEPTED)
async def calculadora(a: int = Query(default=6, gt=5),
                       b: int = Query(default=101, gt=10),
                       x_geek: str = Header(default=None),
                       c: Optional[int] = 0):
    print({'header': x_geek})
    return {'soma': a + b + c}
```
- **Responsabilidade**: Realiza a soma de até três números e registra cabeçalhos.
- **Lógica**:
  1. Valida os valores `a` e `b` com limites mínimos.
  2. Soma os valores fornecidos.
  3. Registra o cabeçalho opcional `x-geek` no console.

---

## Fluxo Completo
1. **Chamada da rota**:
   - Uma dependência (`fake_db`) é executada, simulando a conexão com o banco.
2. **Validações**:
   - Validações de parâmetros (Path, Query, Header) e corpo da requisição são executadas automaticamente pelo FastAPI.
3. **Execução da lógica**:
   - Manipulação da lista `cursos` (CRUD) ou cálculos.
4. **Resposta**:
   - A resposta é retornada ao cliente, com validação de tipo baseada nos modelos.

