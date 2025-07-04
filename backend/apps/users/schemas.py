from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str] = None
    birthdate: Optional[date] = None
    bio: Optional[str] = None
    language: str = "en"
    timezone: str = "UTC"

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: Optional[str] = None
    birthdate: Optional[date] = None
    password: str  

class UserRead(UserBase):
    id: int

    is_superuser: bool
    is_active: bool

    class Config:
        orm_mode = True
