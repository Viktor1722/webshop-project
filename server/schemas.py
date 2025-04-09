from pydantic import BaseModel
from typing import Optional
# This file defines data validation and structure using Pydantic models.
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: str
  
class ProductVariantCreate(BaseModel): 
    size: str
    stock: int

class ProductImageCreate(BaseModel):
    image_url: str
    alt_text: Optional[str] = None
    order: Optional[int] = 0

class ProductDetailCreate(BaseModel):
    materials: Optional[str] = None
    care_instructions: Optional[str] = None
    sizing_guide_url: Optional[str] = None  

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
