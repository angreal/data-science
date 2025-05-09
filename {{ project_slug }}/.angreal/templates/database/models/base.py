"""
Base model classes with common fields and behaviors.

This module provides base classes that can be used to create
models with standard fields like timestamps, etc.
"""

from sqlalchemy import Column, Integer, DateTime, func
import datetime


class TimestampMixin:
    """
    Mixin that adds created_at and updated_at columns.
    """
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, 
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


class IdMixin:
    """
    Mixin that adds an integer id primary key.
    """
    id = Column(Integer, primary_key=True, autoincrement=True)


class BaseModel(IdMixin, TimestampMixin):
    """
    Base model with ID and timestamp fields.
    
    Inherit from this class to create standard models with
    id, created_at, and updated_at fields.
    
    Example:
        ```python
        class User(BaseModel):
            __tablename__ = 'users'
            
            name = Column(String, nullable=False)
            email = Column(String, unique=True)
        ```
    """
    __abstract__ = True
