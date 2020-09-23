from pydantic import BaseModel

class ServidorBase(BaseModel): 
     NOME: str
     SENHA: str
     SECRETARIA: str

class ServidorCreate(ServidorBase):
     pass
  
class Servidor(ServidorBase):
     ID_SERVIDOR: int
     
     class Config:
          orm_mode = True   

  
  
'''
class ServidorBase(BaseModel): 
     NOME: str

class ServidorCreate(ServidorBase): 
       SENHA: str
       SECRETARIA: str

class Servidor(ServidorBase):
     ID_SERVIDOR: int
     SENHA: str
     SECRETARIA: str

     class Config:
          orm_mode = True
   '''