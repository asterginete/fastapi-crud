from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Item as ItemModel
from app.schemas import Item, ItemCreate
from app.crud import item as item_crud
from app.deps import get_db, get_current_user

router = APIRouter()

@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return item_crud.create_item(db=db, item=item, user_id=current_user.id)
