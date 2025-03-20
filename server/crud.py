from sqlalchemy.orm import Session
from database.models import Product
from schemas import ProductCreate, ProductUpdate

def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict()) #converts the product = model from the schemas request to an actual product = dictionary 
    db.add(new_product) #adds the new product to the session
    db.commit() # commits it to the db 
    db.refresh(new_product) #updates the object in the bd in this case the columns 
    return new_product

def get_products(db: Session, skip: int = 0, limit: int = 10): #gets all of the products 
    return db.query(Product).offset(skip).limit(limit).all() #skips the first one and limits them 

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    product = db.query(Product).filter(Product.id == product_id).first() #filter the product 
    if product:
        for key, value in product_data.dict(exclude_unset=True).items(): #if the products exists loop through the data and update the given fields
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product
