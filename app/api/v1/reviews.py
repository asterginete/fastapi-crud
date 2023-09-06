from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Item as ItemModel
from app.schemas import Review, ReviewCreate
from app.crud import review as review_crud
from app.deps import get_db, get_current_user

router = APIRouter()

@router.get("/reviews/{item_id}", response_model=List[Review])
def read_reviews(item_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return review_crud.get_reviews_by_item(db, item_id=item_id, skip=skip, limit=limit)

@router.post("/reviews/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return review_crud.create_review(db=db, review=review)
