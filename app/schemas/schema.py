from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ServidorBase(BaseModel):
     MATRICULA: int
     NOME: str
     SENHA: str
     SECRETARIA: str
     
class ServidorCreate(ServidorBase): 
     SENHA: str
     SECRETARIA: str
        
class Servidor(ServidorBase):
     MATRICULA: int
     
     class Config:
          orm_mode = True   

 
class PessoaBase(BaseModel):
    NOME : str
    CIDADE : str
    ENDERECO : str
    BAIRRO : str
    CONTATO: str
    CPFCNPJ: str
    CATEGORIA: str 
 
class PessoaCreate(PessoaBase): 
     pass

class Pessoa(PessoaBase): 
     NUMERO_CADASTRO : int
     
     class Config: 
          orm_mode = True
 
 
class ProcedimentoBase(BaseModel): 
     NOME_PROCEDIMENTO: str
     
class ProcedimentoCreate(ProcedimentoBase):
     pass 
 
class Procedimento(ProcedimentoBase): 
     ID_PROCEDIMENTO: int
     
     class Config:
          orm_mode = True
  
class AtividadeBase(BaseModel):
     NOME_ATIVIDADE: str
     CNAE: str
      
class AtividadeCreate(AtividadeBase):
     pass 

class Atividade(AtividadeBase):
     ID_ATIVIDADE: int
     
     class Config:
          orm_mode = True       
          
class AtendimentoBase(BaseModel):
     DATA: datetime
     ID_SERVIDOR: int 
     SERVIDOR: List[Servidor] 
     ID_PESSOA: int  
     PESSOA: List[Pessoa] 
     
class AtendimentoCreate(AtendimentoBase):
     DATA: datetime
     
     