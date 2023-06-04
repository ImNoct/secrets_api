from jose import jwt
# from datetime import datetime, timedelta
from secrets import token_urlsafe

from .config import config

def generate_key():
    return token_urlsafe(32)

def encode(data: dict):
    return jwt.encode(data, config.secret_key, algorithm=config.algorithm)

def decode(data: str):
    return jwt.decode(data, config.secret_key, algorithms=[config.algorithm])

