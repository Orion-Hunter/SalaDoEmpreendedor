from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import  cruds.Atendimento as Atendimento
from databases.connectMysql import get_db
from schemas import schema


router = APIRouter()

@router.get("/atendimentos", tags=["/atendimentos"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = Atendimento.get_atendimentos(db, skip=skip, limit=limit)
        return {"atendimentos": rec}

@router.post("/atendimentos", response_model= schema.AtendimentoCreate)
def create(atendimento: schema.AtendimentoCreate, db: Session = Depends(get_db)):
        db_atendimento = Atendimento.create_atendimento(db,atendimento)
        if  db_atendimento is None:
            raise HTTPException(status_code=404, detail="atividade não Cadastrada")
        return db_atendimento 