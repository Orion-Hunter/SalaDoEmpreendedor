from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import  cruds.Pessoa as Pessoa
from databases.connectMysql import get_db
from schemas import schema

router = APIRouter()

@router.get("/pessoas", tags=["pessoas"])
async def  get_all(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
        rec = Pessoa.get_pessoas(db, skip=skip, limit=limit)
        return {"pessoas": rec}
    
@router.get("/pessoas/{numero_cadastro}", response_model= schema.Pessoa)
def get_by_id(numero_cadastro: int, db: Session = Depends(get_db)):
       db_pessoa = Pessoa.get_pessoa(db, numero_cadastro)
       if  db_pessoa is None:
           raise HTTPException(status_code=404, detail="Pessoa não Encontrada!")
       return db_pessoa       
    
@router.post("/pessoas", response_model=schema.Pessoa)
def create(pessoa: schema.PessoaCreate, db: Session = Depends(get_db)):
    db_pessoa = Pessoa.create_pessoa(db,pessoa)
    if  db_pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não Cadastrada")
    return db_pessoa
 
 
@router.delete("/pessoas/{numero_cadastro}")
def delete(numero_cadastro: int, db: Session = Depends(get_db)):
        db_pessoa = Pessoa.delete_pessoa(db, numero_cadastro=numero_cadastro)
        if  db_pessoa is None:
                raise HTTPException(status_code=404, detail="Pessoa não Deletada!")
        return db_pessoa   

@router.put("/pessoas/{numero_cadastro}")
async def  update(pessoa: schema.PessoaCreate, numero_cadastro: int, db: Session = Depends(get_db)):
        db_pessoa  = Pessoa.update_pessoa(db, numero_cadastro=numero_cadastro, new_data=pessoa)
        if  db_pessoa is None:
            raise HTTPException(status_code=404, detail="Pessoa não Atualizada!")
        return db_pessoa    