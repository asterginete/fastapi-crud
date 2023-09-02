from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, String, Text
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    rating = Column(Float, nullable=False)  # e.g., a rating out of 5
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="reviews")
    item = relationship("Item", back_populates="reviews")
