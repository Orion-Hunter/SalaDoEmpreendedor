from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import model
from schemas import schema
from pydantic import  ValidationError
import cruds.Servidor as Servidor
import cruds.Pessoa as Pessoa


def get_atendimentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Atendimento).offset(skip).limit(limit).all()

