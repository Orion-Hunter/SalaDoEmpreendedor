from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema
from pydantic import  ValidationError
    

def get_atividade(db: Session, id_atividade: int):
      return db.query(model.Atividade).filter(model.Atividade.ID_ATIVIDADE == id_atividade).first()

def get_atividades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Atividade).offset(skip).limit(limit).all()

#Erro de Validação
def create_atividade(db: Session, atividade: schema.AtividadeCreate):
        try:
            db_atividade = model.Atividade(NOME_ATIVIDADE=atividade.NOME_ATIVIDADE, CNAE=atividade.CNAE)
            db.add(db_atividade)
            db.commit()
            db.refresh(db_atividade)
            return db_atividade
        except ValidationError as e:
            return e
            #raise HTTPException(status_code=404, detail="Informações inseridas incorretamente!")
 

def delete_atividade(db: Session, id_atividade: int):
        db_atividade = get_atividade(db, id_atividade)
        if db_atividade is None:
            return {"erro": "Esta atividade não está cadastrada!"}
        else:
            db.delete(db_atividade) 
            db.commit()
            return {"id_atividade":  id_atividade ,"mensagem": "atividade Excluído!"}
