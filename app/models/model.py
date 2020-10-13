from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from databases import database

Base =  database.Base


class Servidor(Base):
    __tablename__="servidores"

    MATRICULA =  Column(Integer, primary_key=True, index=True, autoincrement=False)
    NOME =  Column(String(50))
    SENHA = Column(String(200), unique=True) 
    SECRETARIA = Column(String(50))
    
class Pessoa(Base):
    __tablename__ = "pessoas"
    
    NUMERO_CADASTRO =  Column(Integer, primary_key=True, index=True)
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
    SECRETARIA = Column(String(50))
        
class Atividade(Base):
    __tablename__ = "atividades"
    
    ID_ATIVIDADE =  Column(Integer, primary_key=True, index=True)
    NOME_ATIVIDADE = Column(String(150))
    CNAE = Column(String(10), nullable=True)


class Atendimento(Base):
    __tablename__ = "atendimentos"
    
    ID_ATENDIMENTO =  Column(Integer, primary_key=True, index=True)
    DATA = Column(DateTime)
    ID_SERVIDOR = Column(Integer, ForeignKey(Servidor.MATRICULA))
    ID_PESSOA = Column(Integer, ForeignKey(Pessoa.NUMERO_CADASTRO))   
    ATIVIDADES = Column(JSON)
    PROCEDIMENTOS = Column(JSON)
    
    