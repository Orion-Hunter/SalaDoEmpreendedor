from fastapi import APIRouter, Depends
from   database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Servidor

router = APIRouter()


def get_db():
    try:
            db = SessionLocal()
            yield db
    finally:
            db.close()   

@router.get("/", tags=["index"])
async def index(db: Session = Depends(get_db)):
        servidores = db.query(Servidor)
        servidores = servidores.all()
        return {"api": "API SSE", "version": "1.0.0", "servidores": servidores}
 