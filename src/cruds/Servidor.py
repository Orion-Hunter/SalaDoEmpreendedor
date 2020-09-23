from sqlalchemy.orm import Session
from models import model
from schemas import schema
import bcrypt

def get_servidor(db: Session, id_servidor: int):
      return db.query(model.Servidor).filter(model.Servidor.ID_SERVIDOR == id_servidor).first()
     
def get_servidores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servidor).offset(skip).limit(limit).all()

def create_servidor(db: Session, servidor: schema.ServidorCreate):
        hashed_password = bcrypt.hashpw(servidor.SENHA.encode('utf-8'), bcrypt.gensalt())
        db_servidor = model.Servidor(NOME=servidor.NOME, SENHA=hashed_password, SECRETARIA=servidor.SECRETARIA)
        db.add(db_servidor)
        db.commit()
        db.refresh(db_servidor)
        return db_servidor
      
             
def delete_servidor(db: Session, id_servidor: int):
        db_servidor = get_servidor(db, id_servidor)
        if db_servidor is None:
            return {"erro": "Este servidor não está cadastrado!"}
        else:
            db.delete(db_servidor) 
            db.commit()
            return {"id_servidor":  id_servidor ,"mensagem": "Servidor Excluído!"}
 
def update_servidor(db: Session, id_servidor: int, new_data: schema.Servidor):
      db_servidor = get_servidor(db, id_servidor=id_servidor)
      new_hashed_password = bcrypt.hashpw(new_data.SENHA.encode('utf-8'), bcrypt.gensalt())
      db_servidor.SENHA = new_hashed_password
      db.add(db_servidor)
      db.commit()
      return db_servidor
