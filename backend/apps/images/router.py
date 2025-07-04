from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/media/images", tags=["users"])

@router.post("/")
async def new_image():
    return JSONResponse({})