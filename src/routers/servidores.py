from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from  cruds.Servidor import get_servidores, get_servidor, create_servidor
from databases.connectMysql import get_db
from schemas import schema

router = APIRouter()


@router.get("/servidores", tags=["servidor"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = get_servidores(db, skip=skip, limit=limit)
        return {"servidores": rec}
    
@router.get("/servidores/{id_servidor}", response_model= schema.Servidor)
def get_by_id(id_servidor: int, db: Session = Depends(get_db)):
       db_servidor = get_servidor(db, id_servidor=id_servidor)
       if  db_servidor is None:
           raise HTTPException(status_code=404, detail="Servidor não Encontrado")
       return db_servidor    
 
@router.post("/servidores", response_model=schema.Servidor)
def  create(servidor: schema.ServidorCreate, db: Session = Depends(get_db)):
        db_servidor  = create_servidor(db, servidor)
        if  db_servidor is None:
               raise HTTPException(status_code=404, detail="Servidor não Cadastrado")
        return db_servidor    
 