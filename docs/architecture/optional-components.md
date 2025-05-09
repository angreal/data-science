# Optional Components

The template includes several optional components that can be enabled during project initialization. This page describes these components and how they integrate with the rest of the template.

## Overview

During project initialization, you can choose to include these optional components:

```
angreal init [TEMPLATE_URL]
```

The initialization process will prompt you with questions about which components to include:

```
Would you like to include database support with migrations? (true/false)
Would you like to include a Streamlit frontend? (true/false)
Would you like to include application deployment scripts? (true/false)
```

## Database Support

The database component adds SQLAlchemy models and Alembic migrations to your project.

### Directory Structure

```
src/package_name/database/
├── __init__.py
├── db.py              # Database connection utilities
├── alembic.ini        # Alembic configuration
├── migrations/        # Alembic migrations
│   ├── __init__.py
│   ├── env.py
│   └── versions/
│       └── __init__.py
├── models/            # SQLAlchemy models
│   ├── __init__.py
│   ├── base.py        # Base model class
│   ├── item.py        # Example item model
│   └── user.py        # Example user model
└── models.py          # Models import for backwards compatibility
```

### Base Model

The database component includes a base model class that all other models inherit from:

```python
# base.py
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """Base model class with common fields and methods."""
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Common methods can be added here
```

### Example Models

The database component includes example models to demonstrate SQLAlchemy usage:

```python
# user.py
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from .base import BaseModel

class User(BaseModel):
    """User model."""
    
    __tablename__ = "users"
    
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    items = relationship("Item", back_populates="owner")
```

### Database Utilities

The database component includes utilities for connecting to the database:

```python
# db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..core.settings import get_settings

settings = get_settings()
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Migrations

The database component includes Alembic migrations for managing database schema changes:

```python
# env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your models here
from src.package_name.database.models.base import Base

# Rest of the Alembic configuration...
```

## Frontend Dashboard

The frontend component adds a Streamlit dashboard to your project.

### Directory Structure

```
frontend/
├── README.md          # Frontend documentation
├── app.py             # Main Streamlit application
└── requirements.txt   # Frontend-specific dependencies
```

### Streamlit Application

The frontend component includes a basic Streamlit application:

```python
# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Import from your package
from src.package_name.data import loading
from src.package_name.models import inference

# Streamlit app configuration
st.set_page_config(
    page_title="Your Project Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.title("Your Project Dashboard")
st.markdown("Description of your dashboard and what it shows.")

# Sidebar for controls
with st.sidebar:
    st.header("Controls")
    # Add controls here
    
# Main content
st.header("Main Content")
# Add content here
```

### Integration with Source Code

The frontend component integrates with your source code package:

```python
# Import from your package
from src.package_name.data import loading
from src.package_name.models import inference
```

This approach encourages you to move data loading, processing, and model inference code to your package, making it reusable across notebooks and the frontend.

## Deployment Tools

The deployment component adds Docker configuration and deployment scripts to your project.

### Directory Structure

```
deployment/
├── Dockerfile         # Docker configuration
├── app.sh             # Application startup script
└── docker-compose.yml # Docker Compose configuration
```

### Dockerfile

The deployment component includes a Dockerfile for containerizing your application:

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install the package
RUN pip install -e .

# Run the application
CMD ["./app.sh"]
```

### Application Startup Script

The deployment component includes a startup script for running your application:

```bash
#!/bin/bash
# app.sh

# Run database migrations
alembic upgrade head

# Start the application
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Docker Compose Configuration

The deployment component includes a Docker Compose configuration for orchestrating services:

```yaml
# docker-compose.yml
version: '3'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Combining Optional Components

These optional components are designed to work together:

- The **database** component provides data storage and retrieval
- The **frontend** component visualizes data and model results
- The **deployment** component packages everything for production

You can choose any combination of these components based on your project needs.

## Adding Components Later

If you don't include a component during initialization, you can add it later by copying the relevant files from the template repository.

For example, to add the database component later:

1. Copy the database directory from the template
2. Update your settings to include database configuration
3. Install any required dependencies

## Customizing Components

Each component is designed to be customizable to fit your specific project requirements:

- **Database**: Add new models, modify existing ones
- **Frontend**: Add new pages, visualizations, controls
- **Deployment**: Modify the Dockerfile, add new services

You can adapt these components as your project evolves without breaking the overall structure.
