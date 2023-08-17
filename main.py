from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from pydantic import BaseModel
from typing import List, Optional
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []

class User(BaseModel):
    username: str
    password: str
    role: str

class UserInDB(User):
    hashed_password: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None

# In-memory storage
items = {}
users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": "$2b$12$KbIt6U2.pSfHZTc1Kj8hNOGKbTwhzdDR0ofaBBJFJx8YwIOZ8RDO.",  # "password"
        "role": "admin"
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(users_db, form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": ["items"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/items/")
async def create_item(item: Item, current_user: User = Depends(get_current_active_user)):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"status": "Item deleted successfully"}

@app.get("/items/search/{name}")
async def search_items_by_name(name: str):
    result = {k: v for k, v in items.items() if v.name == name}
    return result

@app.patch("/items/{item_id}/name")
async def update_item_name(item_id: int, name: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id].name = name
    return items[item_id]

@app.patch("/items/{item_id}/description")
async def update_item_description(item_id: int, description: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id].description = description
    return items[item_id]

@app.get("/items/count")
async def count_items():
    return {"count": len(items)}

@app.delete("/items/")
async def delete_all_items():
    items.clear()
    return {"status": "All items deleted successfully"}

