from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

####Schemas Servidor
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

 ###Schemas pessoa
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
 
 #schema procedimento
class ProcedimentoBase(BaseModel): 
     NOME_PROCEDIMENTO: str
     SECRETARIA: str
     
class ProcedimentoCreate(ProcedimentoBase):
     pass 
 
class Procedimento(ProcedimentoBase): 
     ID_PROCEDIMENTO: int
     
     class Config:
          orm_mode = True

##schema atividades
class AtividadeBase(BaseModel):
     NOME_ATIVIDADE: str
     CNAE: str
      
class AtividadeCreate(AtividadeBase):
     pass 

class Atividade(AtividadeBase):
     ID_ATIVIDADE: int
     
     class Config:
          orm_mode = True       

#schema atendimento          
class AtendimentoBase(BaseModel):
     DATA: datetime
     ID_SERVIDOR: int 
     ID_PESSOA: int  
     
class AtendimentoCreate(AtendimentoBase):
     ATIVIDADES: List[Atividade]
     PROCEDIMENTOS: List[Procedimento]

class Atendimento(AtividadeBase):
       ID_ATENDIMENTO: int 
       SERVIDOR: Servidor
       PESSOA: Pessoa
       
       class Config:
            orm_mode= True    