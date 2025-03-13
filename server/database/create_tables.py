from server.database.database import engine
from server.database.models import Base

Base.metadata.create_all(bind=engine)
print("Tables created")