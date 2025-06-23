"""
create_db.py - v1.8.0
Run this once to initialize the database schema.

Contributions:
- Uses Base metadata to create all tables in SQLite
"""

from database import Base, engine
from models.recipe import Recipe

Base.metadata.create_all(bind=engine)
print("✅ Database schema created.")
