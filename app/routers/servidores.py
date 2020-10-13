#Arquivo de rotas para realizar as operações com a entidade Servidor

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import  cruds.Servidor as Servidor
from databases.connectMysql import get_db
from schemas import schema

router = APIRouter()


@router.get("/servidores", tags=["servidor"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = Servidor.get_servidores(db, skip=skip, limit=limit)
        return {"servidores": rec}
 
 
@router.get("/servidores/{matricula}/{senha}", response_model= schema.Servidor)
def init_session(matricula: int, senha: str, db: Session = Depends(get_db)):
        db_servidor  = Servidor.login(db, matricula=matricula,senha=senha)
        if  db_servidor is None:
            raise HTTPException(status_code=404, detail="Servidor não encontrado! Verifique se as credenciais foram inseridas corretamente!")
        return db_servidor
    
@router.get("/servidores/{matricula}", response_model= schema.Servidor)
def get_by_id(matricula: int, db: Session = Depends(get_db)):
       db_servidor = Servidor.get_servidor(db,matricula=matricula)
       if  db_servidor is None:
           raise HTTPException(status_code=404, detail="Servidor não Encontrado")
       return db_servidor    
 
@router.post("/servidores", response_model=schema.Servidor)
def  create(servidor: schema.ServidorCreate, db: Session = Depends(get_db)):
        db_servidor  = Servidor.create_servidor(db, servidor)
        if  db_servidor is None:
               raise HTTPException(status_code=404, detail="Servidor não Cadastrado")
        return db_servidor    

@router.delete("/servidores/{matricula}")
def delete(matricula: int, db: Session = Depends(get_db)):
        db_servidor = Servidor.delete_servidor(db, matricula=matricula)
        if  db_servidor is None:
                raise HTTPException(status_code=404, detail="Servidor não Deletado!")
        return db_servidor   

@router.put("/servidores/{matricula}")
def  update(servidor: schema.ServidorCreate, matricula: int, db: Session = Depends(get_db)):
        db_servidor  = Servidor.update_servidor(db, matricula=matricula, new_data=servidor)
        if  db_servidor is None:
               raise HTTPException(status_code=404, detail="Servidor não Atualizado")
        return db_servidor    