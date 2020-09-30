from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import cruds.Servidor as cs
from databases.connectMysql import get_db
from schemas import schema
from models import model

router = APIRouter()


@router.get("/servidores", tags=["servidor"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = cs.get_servidores(db, skip=skip, limit=limit)
        return {"servidores": rec}

   
@router.get("/servidores/{id_servidor}", response_model= schema.Servidor)
def get_by_id(id_servidor: int, db: Session = Depends(get_db)):
       db_servidor = cs.get_servidor(db, id_servidor=id_servidor)
       if  db_servidor is None:
           raise HTTPException(status_code=404, detail="Servidor não Encontrado")
       return db_servidor    


@router.post("/servidores", response_model=schema.Servidor)
def  create(servidor: schema.ServidorCreate, db: Session = Depends(get_db)):
        db_servidor  = cs.create_servidor(db, servidor)
        return db_servidor    

@router.delete("/servidores/{id_servidor}")
def delete(id_servidor: int, db: Session = Depends(get_db)):
        db_servidor = cs.delete_servidor(db, id_servidor=id_servidor)
        if  db_servidor is None:
                raise HTTPException(status_code=404, detail="Servidor não Deletado!")
        return db_servidor   

@router.put("/servidores/{id_servidor}")
def  update(servidor: schema.ServidorCreate, id_servidor: int, db: Session = Depends(get_db)):
        db_servidor  = cs.update_servidor(db, id_servidor=id_servidor, new_data=servidor)
        if  db_servidor is None:
               raise HTTPException(status_code=404, detail="Servidor não Atualizado")
        return db_servidor    
