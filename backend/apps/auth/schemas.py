from pydantic import BaseModel, field_validator
from typing import Literal

class ObtainTokensRequest(BaseModel):
    identifier: str
    password: str

class Payload(BaseModel):
    sub: str
    jti: str | None = None
    exp: float | None = None

    token_type: Literal["access", "refresh"]
    
    @field_validator("sub", mode="before")
    @classmethod
    def convert_sub_to_str(cls, v):
        return str(v)