from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Order).filter(models.Order.user_id == user_id).offset(skip).limit(limit).all()
