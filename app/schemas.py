from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class SecretIn(BaseModel):
    text: str
    code: str

class SecretKey(BaseModel):
    key: str

class AskSecret(BaseModel):
    code: str

class SecretOut(BaseModel):
    text: str
