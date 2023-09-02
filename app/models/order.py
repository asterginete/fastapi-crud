from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, Table, String
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(Float)
    status = Column(String, default="pending")  # e.g., "pending", "shipped", "delivered"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="orders")
    items = relationship("Item", secondary="order_items", back_populates="orders")

# Association table for many-to-many relationship between Item and Order
order_items = Table(
    "order_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True),
    Column("quantity", Integer, default=1)  # Number of items of this type in the order
)
