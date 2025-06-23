"""
models/recipe.py - v1.8.0
SQLAlchemy model for the Recipe table.

Contributions:
- Defines the structure of the 'recipes' table
- Replaces JSON structure for database storage
"""

from sqlalchemy import Column, Integer, String
from database.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    ingredients = Column(String)
    steps = Column(String)
    category = Column(String)
