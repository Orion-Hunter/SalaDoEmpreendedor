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