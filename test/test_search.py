from databases.connectMysql import get_db
from cruds.Servidor import authenticate_user
from schemas.schema import ServidorAuthenticate 


def test():
    g = ServidorAuthenticate(NOME="Fabrício", SENHA="12345")
    return authenticate_user(get_db(),g)
