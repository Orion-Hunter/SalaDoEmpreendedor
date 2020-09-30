from pydantic import BaseModel
from typing import Optional

class ServidorBase(BaseModel):
     NOME: str
     SENHA: str
     SECRETARIA: str
     
class ServidorCreate(ServidorBase): 
     SENHA: str
     SECRETARIA: str
  
class ServidorInfoBase(BaseModel): 
     NOME: str

class ServidorAuthenticate(ServidorInfoBase): 
     SENHA: str  

class Token(BaseModel): 
     access_token: str
     token_type: str

class TokenData(BaseModel): 
     username: Optional[str] = None

      
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