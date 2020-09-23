from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema
import bcrypt

def get_servidor(db: Session, id_servidor: int):
      return db.query(model.Servidor).filter(model.Servidor.ID_SERVIDOR == id_servidor).first()
                
def get_servidores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servidor).offset(skip).limit(limit).all()

def create_servidor(db: Session, servidor: schema.ServidorCreate):
        try:
            db_servidor = model.Servidor(NOME=servidor.NOME, SENHA=servidor.SENHA, SECRETARIA=servidor.SECRETARIA)
            db.add(db_servidor)
            db.commit()
            db.refresh(db_servidor)
            return db_servidor
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail=" A senha informada não está disponível!")
             
def delete_servidor(db: Session, id_servidor: int):
        db_servidor = get_servidor(db, id_servidor)
        if db_servidor is None:
            return {"erro": "Este servidor não está cadastrado!"}
        else:
            db.delete(db_servidor) 
            db.commit()
            return {"id_servidor":  id_servidor ,"mensagem": "Servidor Excluído!"}

def update_servidor(db: Session, id_servidor: int, new_data: schema.ServidorCreate):
        try:
            db_servidor = get_servidor(db, id_servidor=id_servidor)
            db_servidor.NOME = new_data.NOME 
            db_servidor.SECRETARIA = new_data.SECRETARIA
            db_servidor.SENHA = new_data.SENHA
            db.add(db_servidor)
            db.commit()        
            return  {"sucess": "Servidor Atualizado com sucesso!"}
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail=" A senha informada não está disponível!")