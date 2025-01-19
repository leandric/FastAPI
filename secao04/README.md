# Cursos API - FastAPI + SQLAlchemy

Este é um projeto de API desenvolvido com **FastAPI**, utilizando **SQLAlchemy** (modo assíncrono) para persistência no banco de dados. O objetivo principal é gerenciar um sistema de cursos, oferecendo operações de CRUD (Create, Read, Update, Delete).

---

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e rápido.
- **SQLAlchemy (Assíncrono):** ORM para manipulação do banco de dados.
- **PostgreSQL:** Banco de dados relacional utilizado no projeto.
- **Docker e Docker Compose:** Para facilitar o deploy e a execução do ambiente de desenvolvimento.
- **Uvicorn:** Servidor ASGI para rodar a aplicação.
- **Pydantic:** Validação de dados e esquemas.
- **pytest:** Para testes automatizados (a ser configurado).

---

## 🚀 Funcionalidades

- **POST /cursos/**  
  Criar um novo curso no sistema.
  
- **GET /cursos/**  
  Listar todos os cursos cadastrados (com possibilidade de paginação futura).

- **GET /cursos/{curso_id}**  
  Obter detalhes de um curso específico.

- **PUT /cursos/{curso_id}**  
  Atualizar informações de um curso existente.

- **DELETE /cursos/{curso_id}**  
  Remover um curso do sistema.

---

## ⚙️ Como Rodar o Projeto

### **Pré-requisitos**
- Docker e Docker Compose instalados.
- Python 3.10+ instalado (opcional, caso rode o projeto fora do Docker).

### **Passo a passo**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Suba os serviços usando o Docker Compose:
   ```bash
   make up
   ```

3. Acesse a aplicação:
   - A API estará disponível em: [http://localhost:8000](http://localhost:8000)
   - A documentação interativa (Swagger) estará disponível em: [http://localhost:8000/docs](http://localhost:8000/docs)

4. Para derrubar os serviços:
   ```bash
   make down
   ```

5. Para limpar volumes e imagens não utilizadas:
   ```bash
   make clean
   ```

---

## 🗂️ Estrutura do Projeto

```plaintext
├── api/
│   └── v1/
│       └── endpoints/
│           └── curso.py       # Rotas para CRUD de cursos
│       └── api.py             # Definição do roteador principal
├── core/
│   ├── configs.py             # Configurações do projeto
│   ├── database.py            # Conexão com o banco de dados
│   └── deps.py                # Dependências (ex.: sessão do banco)
├── models/
│   └── curso_model.py         # Modelo SQLAlchemy do Curso
├── schemas/
│   └── curso_schema.py        # Esquema Pydantic para validação de dados
├── main.py                    # Arquivo principal da aplicação
├── dockerfile                 # Configuração do Docker
├── compose.yaml               # Configuração do Docker Compose
├── criar_tabelas.py           # Script para criar tabelas no banco
├── requirements.txt           # Dependências do projeto
├── Makefile                   # Comandos de automação
```

---

## 🐳 Comandos Úteis (Makefile)

- **`make up`**: Sobe os serviços (API + Banco de Dados).
- **`make down`**: Derruba os serviços.
- **`make restart`**: Reinicia os serviços.
- **`make clean`**: Remove volumes e imagens não utilizados.
- **`make logs`**: Exibe os logs do banco de dados.