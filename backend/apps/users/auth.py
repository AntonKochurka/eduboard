from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/obtain")
async def obtain_pair():
    return JSONResponse({})