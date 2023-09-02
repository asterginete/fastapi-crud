from pydantic import BaseModel
from datetime import datetime

class ReviewBase(BaseModel):
    user_id: int
    item_id: int
    rating: float
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
