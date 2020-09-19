from sqlalchemy import Column, Integer, String
from databases.database import Base

class Servidor(Base):
    __tablename__="servidor"

    ID_SERVIDOR =  Column(Integer, primary_key=True, index=True)
    NOME =  Column(String)
    SENHA = Column(String, unique=True) 
    SECRETARIA = Column(String)