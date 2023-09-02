from sqlalchemy.orm import Session
from . import models, schemas

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews_by_item(db: Session, item_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.item_id == item_id).offset(skip).limit(limit).all()
