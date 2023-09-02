from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core import security
from app.crud import user as user_crud
from app.models import User as UserModel
from app.schemas import TokenData
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.verify_token(token, SECRET_KEY, ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except:
        raise credentials_exception
    user = user_crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
