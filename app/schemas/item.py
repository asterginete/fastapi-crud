from pydantic import BaseModel
from datetime import datetime
from typing import List

class ItemBase(BaseModel):
    name: str
    description: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True
