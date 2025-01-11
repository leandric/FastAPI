from fastapi import FastAPI

from routes.curso_router import router as curso_router
from routes.usuario_router import router as usuario_router

app = FastAPI()
app.include_router(curso_router, tags=['cursos'])
app.include_router(usuario_router, tags=['users'])

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='debug', reload=True)