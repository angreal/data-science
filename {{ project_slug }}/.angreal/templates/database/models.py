from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

# Define your models here
# Example:
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String, unique=True)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
