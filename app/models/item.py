from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    owner = relationship("User", back_populates="items")
    reviews = relationship("Review", back_populates="item")
    orders = relationship("Order", secondary="order_items", back_populates="items")

# Association table for many-to-many relationship between Item and Order
order_items = Table(
    "order_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True)
)
