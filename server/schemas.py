from pydantic import BaseModel
from typing import Optional
# This file defines data validation and structure using Pydantic models.
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: str
    # stock: Optional[int] = 0
    # size: str
    # category: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
