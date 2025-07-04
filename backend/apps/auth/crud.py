from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import BlacklistedToken
from .services import decode_token

async def blacklist_token(*, token: str, token_type: str, db: AsyncSession) -> BlacklistedToken:
    jti = decode_token(token)["jti"]
    token = BlacklistedToken(jti=jti, token_type=token_type)
    
    db.add(token)
    
    await db.commit()
    await db.refresh(token)

    return token

async def is_token_blacklisted(token: str, db: AsyncSession) -> bool:
    jti = decode_token(token)["jti"]
    result = await db.execute(
        select(BlacklistedToken).where(BlacklistedToken.jti == jti)
    )
    
    return result.scalar_one_or_none() is not None
