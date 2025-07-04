from sqlalchemy import Column, String, Integer 

from core.database import Base
from utils.mixins import BaseMixin

class Image(Base, BaseMixin):
    __tablename__ = "images"

    filename = Column(String(256), unique=True, nullable=False)
    original_name = Column(String(256), nullable=False)
    content_type = Column(String(64), nullable=False)
    size = Column(Integer, nullable=True)