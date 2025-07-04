from sqlalchemy import Column, String
from core.database import Base
from utils.mixins import BaseMixin

class BlacklistedToken(Base, BaseMixin):
    __tablename__ = "blacklisted_token"

    jti = Column(String, unique=True, index=True, nullable=False)  
    token_type = Column(String, nullable=False)  
