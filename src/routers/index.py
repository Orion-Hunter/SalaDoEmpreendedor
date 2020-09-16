from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["index"])
async def index():
    return {"api": "API SSE", "version": "1.0.0"}