"""
database.py - v1.8.0
Sets up the SQLAlchemy engine, session, and base model class.

Contributions:
- engine: connects to SQLite database
- Base: declarative base for all models
- SessionLocal: creates session objects to run DB operations
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database in the /data directory
engine = create_engine("sqlite:///data/recipes.db", echo=True)

# Base class for model definitions
Base = declarative_base()

# Session maker bound to the engine
SessionLocal = sessionmaker(bind=engine)
