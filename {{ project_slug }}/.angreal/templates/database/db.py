"""
Database connection module.

This module provides database connection utilities including the engine,
session factory, and session dependency.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from ..core.config import get_settings

settings = get_settings()

# Create engine based on configuration
engine = create_engine(settings.DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Get a database session.
    
    Yields:
        Session: A SQLAlchemy session
        
    Example:
        ```python
        # When used with FastAPI
        @app.get("/users/")
        def read_users(db: Session = Depends(get_db)):
            users = db.query(User).all()
            return users
        ```
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
