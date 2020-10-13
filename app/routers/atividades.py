from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import  cruds.Atividade as Atividade
from databases.connectMysql import get_db
from schemas import schema

router = APIRouter()

@router.get("/atividades", tags=["atividades"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = Atividade.get_atividades(db, skip=skip, limit=limit)
        return {"atividades": rec}
    
@router.post("/atividades", response_model=schema.AtividadeCreate)
def create(atividade: schema.AtividadeCreate, db: Session = Depends(get_db)):
    db_atividade = Atividade.create_atividade(db,atividade)
    if  db_atividade is None:
        raise HTTPException(status_code=404, detail="atividade não Cadastrada")
    return db_atividade
 
 
@router.delete("/atividades/{id_atividade}")
def delete(id_atividade: int, db: Session = Depends(get_db)):
        db_atividade = Atividade.delete_atividade(db, id_atividade=id_atividade)
        if  db_atividade is None:
                raise HTTPException(status_code=404, detail="Atividade não Deletada!")
        return db_atividade   
