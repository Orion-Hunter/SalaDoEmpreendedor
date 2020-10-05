from fastapi import Depends, FastAPI
import uvicorn
from routers import  servidores, pessoas, procedimentos, atividades, atendimentos


app = FastAPI()

@app.get("/")
def index():
    return {"api": "API SSE", "version": "1.0.0"}
     
app.include_router(servidores.router)
app.include_router(pessoas.router)
app.include_router(procedimentos.router)
app.include_router(atividades.router)
app.include_router(atendimentos.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
