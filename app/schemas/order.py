from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.schemas.product import ProductResponse


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    product: ProductResponse

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    total: float
    created_at: datetime
    items: list[OrderItemResponse]

    class Config:
        from_attributes = True