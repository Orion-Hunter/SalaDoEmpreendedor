from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema
import bcrypt

    
#Busca um Servidor pelo ID
def get_servidor(db: Session, matricula: int):
      return db.query(model.Servidor).filter(model.Servidor.MATRICULA == matricula).first()

#Retorna todos os servidores cadastrados                
def get_servidores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servidor).offset(skip).limit(limit).all()

#Cadastra um servidor
def create_servidor(db: Session, servidor: schema.ServidorCreate):
        try:
            db_servidor = model.Servidor(MATRICULA=servidor.MATRICULA, NOME=servidor.NOME, SENHA=servidor.SENHA, SECRETARIA=servidor.SECRETARIA)
            db.add(db_servidor)
            db.commit()
            db.refresh(db_servidor)
            return db_servidor
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail=" A senha informada não está disponível!")
 
#Exclui um servidor             
def delete_servidor(db: Session, matricula: int):
        db_servidor = get_servidor(db, matricula)
        if db_servidor is None:
            return {"erro": "Este servidor não está cadastrado!"}
        else:
            db.delete(db_servidor) 
            db.commit()
            return {"Número da Matrícula":  matricula ,"mensagem": "Servidor Excluído!"}

#Atualiza um servidor
def update_servidor(db: Session, matricula: int, new_data: schema.ServidorCreate):
        try:
            db_servidor = get_servidor(db, matricula=matricula)
            db_servidor.NOME = new_data.NOME 
            db_servidor.SECRETARIA = new_data.SECRETARIA
            db_servidor.SENHA = new_data.SENHA
            db.add(db_servidor)
            db.commit()        
            return  {"sucess": "Servidor Atualizado com sucesso!"}
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail=" A senha informada não está disponível!")