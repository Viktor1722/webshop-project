from server.database.database import get_db
from server.database.models import Product

db = next(get_db())

products = db.query(Product).all()

for product in products:
    print(f"{product.id}: {product.name} - {product.price}€")
