import jwt

from datetime import datetime, timedelta, timezone
from .schemas import Payload
from core.settings import settings


def generate_token(payload: Payload) -> tuple[str, float]:
    now = datetime.now(tz=timezone.utc)

    if payload.token_type == "access":
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    elif payload.token_type == "refresh":
        expire = now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    else:
        raise ValueError("Invalid token type")

    payload.exp = int(expire.timestamp())

    token = jwt.encode(
        payload.model_dump(),
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token, payload.exp

def decode_token(token):
    return jwt.decode(
        token, 
        key=settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )