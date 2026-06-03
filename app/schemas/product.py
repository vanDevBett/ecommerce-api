from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True