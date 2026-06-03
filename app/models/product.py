from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    order_items = relationship("OrderItem", back_populates="product")