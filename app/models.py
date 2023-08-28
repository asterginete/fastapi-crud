from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

Base = declarative_base()

class UserInDB(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

class ItemInDB(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    owner = relationship("UserInDB", back_populates="items")

UserInDB.items = relationship("ItemInDB", back_populates="owner")
