import jwt
import uuid

from datetime import datetime, timedelta, timezone
from . import crud, schemas

from core.database import AsyncSession
from core.settings import settings


def generate_token(payload: schemas.Payload) -> tuple[str, float]:
    now = datetime.now(tz=timezone.utc)

    if payload.token_type == "access":
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    elif payload.token_type == "refresh":
        expire = now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    else:
        raise ValueError("Invalid token type")

    payload.exp = int(expire.timestamp())
    payload.jti = str(uuid.uuid4())

    token = jwt.encode(
        payload.model_dump(),
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token, payload.exp

def decode_token(token: str) -> dict:
    return jwt.decode(
        token, 
        key=settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

async def is_token_blacklisted(token: str, session: AsyncSession) -> bool:
    jti = decode_token(token)["jti"]
    return await crud.is_jti_blacklisted(jti=jti, session=session)

async def blacklist_token(*, token: str, token_type: str, session: AsyncSession):
    jti = decode_token(token)["jti"]
    return await crud.blacklist_jti(jti=jti, token_type=token_type, session=session)