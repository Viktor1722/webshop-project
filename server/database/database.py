from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection string
DATABASE_URL = "postgresql://postgres:bmwe46@localhost:5433/e-commerce"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Test connection
try:
    with engine.connect() as conn:
        print("Database connected successfully!")
except Exception as e:
    print("Database connection error:", e)
