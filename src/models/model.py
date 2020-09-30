from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from databases import database

Base =  database.Base


class Servidor(Base):
    __tablename__="servidores"

    ID_SERVIDOR =  Column(Integer, primary_key=True, index=True)
    NOME =  Column(String(50))
    SENHA = Column(String(200), unique=True) 
    SECRETARIA = Column(String(50))
    
class Pessoa(Base):
    __tablename__ = "pessoas"
    
    ID_PESSOA =  Column(Integer, primary_key=True, index=True)
    NOME =  Column(String(50))
    CIDADE = Column(String(50))
    ENDERECO = Column(String(100))
    BAIRRO = Column(String(30))
    CONTATO = Column(String(20))
    CPFCNPJ = Column(String(20))
    CATEGORIA = Column(String(50))

class Procedimento(Base):
    __tablename__ = "procedimentos"
    
    ID_PROCEDIMENTO =  Column(Integer, primary_key=True, index=True)
    NOME_PROCEDIMENTO = Column(String(150))
        
class Atividade(Base):
    __tablename__ = "atividades"
    
    ID_ATIVIDADE =  Column(Integer, primary_key=True, index=True)
    NOME_ATIVIDADE = Column(String(150))
    CNAE = Column(String(10))

'''
class Atendimento(Base):
    __tablename__ = "atendimentos"
    
    ID_ATENDIMENTO =  Column(Integer, primary_key=True, index=True)
    DATA = Column(DateTime)
    SERVIDOR = Column(Integer, ForeignKey(Servidor.ID_SERVIDOR))
    PESSOA = Column(Integer, ForeignKey(Pessoa.ID_PESSOA))
    PROCEDIMENTOS = Column(Integer)
 '''   
    