from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import cruds.Procedimento as Procedimento
from databases.connectMysql import get_db
from schemas import schema

router = APIRouter()


@router.get("/procedimentos", tags=["procedimentos"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = Procedimento.get_procedimentos(db, skip=skip, limit=limit)
        return {"procedimentos": rec}
    
@router.get("/procedimentos/{id_procedimento}", response_model= schema.Procedimento)
def get_by_id(id_procedimento: int, db: Session = Depends(get_db)):
       db_procedimento = Procedimento.get_procedimento(db, id_procedimento)
       if  db_procedimento is None:
           raise HTTPException(status_code=404, detail="procedimento não Encontrado")
       return db_procedimento    
 
@router.post("/procedimentos", response_model=schema.Procedimento)
def  create(procedimento: schema.ProcedimentoCreate, db: Session = Depends(get_db)):
        db_procedimento  = Procedimento.create_procedimento(db, procedimento)
        if  db_procedimento is None:
               raise HTTPException(status_code=404, detail="procedimento não Cadastrado")
        return db_procedimento    

@router.delete("/procedimentos/{id_procedimento}")
def delete(id_procedimento: int, db: Session = Depends(get_db)):
        db_procedimento = Procedimento.delete_procedimento(db, id_procedimento)
        if  db_procedimento is None:
                raise HTTPException(status_code=404, detail="procedimento não Deletado!")
        return db_procedimento   

@router.put("/procedimentos/{id_procedimento}")
def  update(procedimento: schema.ProcedimentoCreate, id_procedimento: int, db: Session = Depends(get_db)):
        db_procedimento  = Procedimento.update_procedimento(db, id_procedimento, new_data=procedimento)
        if  db_procedimento is None:
               raise HTTPException(status_code=404, detail="procedimento não Atualizado")
        return db_procedimento    