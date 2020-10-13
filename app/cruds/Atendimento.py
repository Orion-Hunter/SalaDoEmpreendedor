## Entity Atendimentos crud functions
'''
Aqui ficam as funções responsáveis por realizarem as operações de escrita e leitura no banco de dados da tabela Atendimentos
'''
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema
from pydantic import  ValidationError
from datetime import datetime
import json

import cruds.Servidor as Servidor
import cruds.Pessoa as Pessoa


###Ler todos os registros de atendimentos
def get_atendimentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Atendimento).offset(skip).limit(limit).all()

def create_atendimento(db: Session, atendimento: schema.AtendimentoCreate):
    try:
        db_atendimento = model.Atendimento()
        db_atendimento.DATA = datetime.now()
        db_atendimento.ID_PESSOA = atendimento.ID_PESSOA
        db_atendimento.ID_SERVIDOR = atendimento.ID_SERVIDOR 
        db_atendimento.ATIVIDADES = json.dumps(atendimento.ATIVIDADES, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print(db_atendimento.PESSOA)
        db_atendimento.PROCEDIMENTOS = json.dumps(atendimento.PROCEDIMENTOS, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        db.add(db_atendimento)
        db.commit()
        db.refresh(db_atendimento)
        return db_atendimento
    except IntegrityError as e:
        raise HTTPException(status_code=404, detail="Informações inseridas incorretamente") 
     