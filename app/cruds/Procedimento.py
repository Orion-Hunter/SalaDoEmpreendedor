from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema

    

def get_procedimento(db: Session, id_Procedimento: int):
      return db.query(model.Procedimento).filter(model.Procedimento.ID_PROCEDIMENTO == id_Procedimento).first()

def get_procedimentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Procedimento).offset(skip).limit(limit).all()

def create_procedimento(db: Session, Procedimento: schema.ProcedimentoCreate):
        try:
            db_Procedimento = model.Procedimento(NOME_PROCEDIMENTO=Procedimento.NOME_PROCEDIMENTO)
            db.add(db_Procedimento)
            db.commit()
            db.refresh(db_Procedimento)
            return db_Procedimento
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail="Informações inseridas incorretamente!")
 

def delete_procedimento(db: Session, id_Procedimento: int):
        db_Procedimento = get_procedimento(db, id_Procedimento)
        if db_Procedimento is None:
            return {"erro": "Este Procedimento não está cadastrado!"}
        else:
            db.delete(db_Procedimento) 
            db.commit()
            return {"id_Procedimento":  id_Procedimento ,"mensagem": "Procedimento Excluído!"}


def update_procedimento(db: Session, id_Procedimento: int, new_data: schema.ProcedimentoCreate):
        try:
            db_Procedimento = get_procedimento(db, id_Procedimento=id_Procedimento)
            db_Procedimento.NOME_PROCEDIMENTO = new_data.NOME_PROCEDIMENTO 
            db.add(db_Procedimento)
            db.commit()        
            return  {"sucess": "Procedimento Atualizado com sucesso!"}
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail="Informações inseridas incorretamente!")