from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import schemas, models
from ..utils import decode
from ..database import get_db

router = APIRouter(
    prefix="/secrets",
    tags=['Secrets']
)

@router.get("/{key}", response_model=schemas.SecretOut, status_code=status.HTTP_200_OK)
def get_secret(key: str, secret: schemas.AskSecret, db: Session = Depends(get_db)):
    result_query = db.query(models.Secret).filter(models.Secret.key == key)
    result = result_query.first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"secret with key: {key} was not found")
    
    secret_decoded = decode(result.data)
    if secret_decoded["code"] != secret.code:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"wrong key or code")
    
    result_query.delete(synchronize_session=False)
    db.commit()
    return { "text" : secret_decoded["text"]}