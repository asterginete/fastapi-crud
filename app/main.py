from fastapi import FastAPI, HTTPException, Depends
from . import models, schemas, crud, deps
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database configuration
DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/mydatabase"
database = Database(DATABASE_URL)
metadata = models.Base.metadata

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: deps.OAuth2PasswordRequestForm = Depends()):
    return await crud.authenticate_user(form_data.username, form_data.password)

@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.Item, current_user: schemas.User = Depends(deps.get_current_active_user)):
    return await crud.create_item(item, current_user.id)

@app.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 10, current_user: schemas.User = Depends(deps.get_current_active_user)):
    return await crud.get_items(skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, current_user: schemas.User = Depends(deps.get_current_active_user)):
    return await crud.get_item(item_id)

# ... [Other routes as needed]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
