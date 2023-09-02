from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderBase(BaseModel):
    user_id: int
    total_price: float
    status: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
