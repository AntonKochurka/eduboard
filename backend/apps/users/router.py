from fastapi import APIRouter
from fastapi.responses import JSONResponse

from . import models, schemas, crud

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def new_user(request: schemas.UserCreate):
    return JSONResponse({})