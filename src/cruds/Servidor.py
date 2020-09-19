from sqlalchemy.orm import Session
from models import model
from schemas import schema


def get_servidor(db: Session, id_servidor: int):
      return db.query(model.Servidor).filter(model.Servidor.ID_SERVIDOR == id_servidor).first()
  
def get_servidores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servidor).offset(skip).limit(limit).all()

def create_servidor(db: Session, servidor: schema.ServidorCreate):
       # res = db.query(model.Servidor).filter(model.Servidor.SENHA == servidor.SENHA)
       # if res is None:
        db_servidor = model.Servidor(NOME=servidor.NOME, SENHA=servidor.SENHA, SECRETARIA=servidor.SECRETARIA)
        db.add(db_servidor)
        db.commit()
        db.refresh(db_servidor)
        return  db_servidor
        #else:
        #    return {"message": "Esta senha não está disponível!"}