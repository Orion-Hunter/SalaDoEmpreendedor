#Arquivo de Conexão ao banco de dados

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


SQALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root123@localhost:3306/sse_test"

engine = create_engine(SQALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()