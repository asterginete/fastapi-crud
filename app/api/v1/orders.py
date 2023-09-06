from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import User as UserModel
from app.schemas import Order, OrderCreate
from app.crud import order as order_crud
from app.deps import get_db, get_current_user

router = APIRouter()

@router.get("/orders/", response_model=List[Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return order_crud.get_orders_by_user(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/orders/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return order_crud.create_order(db=db, order=order)
