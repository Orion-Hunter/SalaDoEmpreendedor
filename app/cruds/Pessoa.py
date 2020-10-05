from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema

def get_pessoa(db: Session, numero_cadastro: int):
      return db.query(model.Pessoa).filter(model.Pessoa.NUMERO_CADASTRO == numero_cadastro).first()


def get_pessoas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Pessoa).offset(skip).limit(limit).all()


def create_pessoa(db: Session, pessoa: schema.PessoaCreate):
        try:
            db_pessoa = model.Pessoa(NOME=pessoa.NOME,  CIDADE = pessoa.CIDADE, ENDERECO = pessoa.ENDERECO, BAIRRO =pessoa.BAIRRO, CONTATO = pessoa.CONTATO, CPFCNPJ = pessoa.CPFCNPJ, CATEGORIA = pessoa.CATEGORIA)
            db.add(db_pessoa)
            db.commit()
            db.refresh(db_pessoa)
            return db_pessoa
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail="Informações inseridas incorretamente")
        
def delete_pessoa(db: Session, numero_cadastro: int):
        db_pessoa = get_pessoa(db, numero_cadastro)
        if db_pessoa is None:
            return {"erro": "Esta pessoa não está cadastrada!"}
        else:
            db.delete(db_pessoa) 
            db.commit()
            return {"Número do Cadastro":  numero_cadastro ,"mensagem": "Pessoa Excluída!"}

def update_pessoa(db: Session, numero_cadastro: int, new_data: schema.PessoaCreate):
        try:
            db_pessoa = get_pessoa(db, numero_cadastro=numero_cadastro)
            db_pessoa.NOME = new_data.NOME 
            db_pessoa.CATEGORIA = new_data.CATEGORIA
            db_pessoa.CONTATO = new_data.CONTATO
            db_pessoa.ENDERECO = new_data.ENDERECO
            db_pessoa.CPFCNPJ = new_data.CPFCNPJ
            db_pessoa.BAIRRO = new_data.BAIRRO
            db_pessoa.CIDADE = new_data.CIDADE
            db.add(db_pessoa)
            db.commit()        
            return  {"sucess": "Pessoa Atualizada com sucesso!"}
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail=" Informações inseridas incorretamente!")