from sqlalchemy import Column, Integer, String
from databases.database import Base

Base = Base

class Servidor(Base):
    __tablename__="servidor"

    ID_SERVIDOR =  Column(Integer, primary_key=True, index=True)
    NOME =  Column(String(50))
    SENHA = Column(String(10), unique=True) 
    SECRETARIA = Column(String(50))