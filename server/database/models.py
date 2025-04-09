from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .database import Base  # This is your existing Base
from sqlalchemy.orm import relationship

Base = declarative_base()

# your existing Product model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    image = Column(String)

    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    details = relationship("ProductDetail", back_populates="product", uselist=False, cascade="all, delete-orphan")

# ProductVariant model
class ProductVariant(Base):
    __tablename__ = "products_sizes"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    size = Column(String, nullable=False)
    stock = Column(Integer, default=0)

    product = relationship("Product", back_populates="variants")

# ProductImage model
class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    url = Column(String, nullable=False)

    product = relationship("Product", back_populates="images")

# ProductDetail model
class ProductDetail(Base):
    __tablename__ = "product_details"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    materials = Column(String)
    size_chart_url = Column(String)

    product = relationship("Product", back_populates="details")
