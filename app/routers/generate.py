from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func


from .. import schemas, models
from ..utils import generate_key, encode, decode
from ..database import get_db


router = APIRouter(
    prefix="/generate",
    tags=['Generate']
)

@router.get("/", response_model=schemas.SecretKey, status_code=status.HTTP_201_CREATED)
def generate(secret: schemas.SecretIn, db: Session = Depends(get_db)):
    key = generate_key()
    while db.query(models.Secret).filter(models.Secret.key == key).first():
        key = generate_key()

    new_secret = models.Secret(key=key, data=encode({"code":secret.code, "text":secret.text}))
    db.add(new_secret)
    db.commit()
    return { "key" : key }
    
    
    