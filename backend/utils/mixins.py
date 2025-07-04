from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declared_attr

class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now()
        )
