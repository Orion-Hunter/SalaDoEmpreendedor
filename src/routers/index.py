from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from  cruds.Servidor import get_servidor, get_servidores, create_servidor

router = APIRouter()



@router.get("/", tags=["index"])
async def index():
        return {"api": "API SSE", "version": "1.0.0"}
 