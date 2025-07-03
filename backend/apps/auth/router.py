from fastapi import APIRouter
from fastapi.responses import JSONResponse

from . import schemas, services

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/obtain")
async def obtain_pair(
    request: schemas.ObtainTokensRequest
):
    refresh, exp = services.generate_token(schemas.Payload(sub=1, token_type="refresh"))
    access, _ = services.generate_token(schemas.Payload(sub=1, token_type="access"))

    response = JSONResponse(
        {
            "refresh": refresh,
            "access": access,
        }
    )

    response.set_cookie(
        key="refresh", value=refresh,
        expires=exp,
        httponly=True, 
        secure=True,
        samesite="strict"
    )

    return response