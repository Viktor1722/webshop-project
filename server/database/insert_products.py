from server.database.database import get_db
from server.database.models import Product

db = next(get_db())

new_product = Product(name="T-shirt", description="A cool cotton T-shirt", price=19.99)

db.add(new_product)
db.commit()

print("Product added!")
