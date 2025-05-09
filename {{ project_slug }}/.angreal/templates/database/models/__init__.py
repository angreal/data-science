"""
Database models package.

This file defines the SQLAlchemy Base and imports all model classes.
When adding new models:
1. Create a new file for your model
2. Import the model here
3. Add it to __all__ list
"""

from sqlalchemy.ext.declarative import declarative_base

# Create base class for declarative models
Base = declarative_base()

# Import models
# Examples:
# from .user import User
# from .item import Item

# Export models
__all__ = [
    'Base',
    # Add your models to this list:
    # 'User',
    # 'Item',
]
