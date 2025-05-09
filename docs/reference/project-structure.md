# Project Structure Reference

This page provides a detailed reference for the complete project structure created by the template, explaining the purpose and contents of each directory and key files.

## Top-Level Structure

```
project_name/
├── .angreal/               # Project tasks and automation
├── docs/                   # Documentation
├── notebooks/              # Jupyter notebooks organized by epochs
├── src/                    # Source code
├── tests/                  # Test suite
├── frontend/               # Streamlit dashboard (optional)
├── deployment/             # Deployment scripts (optional)
├── .gitignore              # Git ignore file
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── mkdocs.yml              # Documentation configuration
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project overview
```

## Detailed Structure

### `.angreal/` - Project Automation

```
.angreal/
├── init.py                 # Initialization script
├── task_documentation.py   # Documentation tasks
├── task_new.py             # Tasks for creating new epochs/notebooks
├── task_new_model.py       # Tasks for creating new database models
├── task_test.py            # Testing tasks
└── templates/              # Template files for project components
    ├── database/           # Database templates
    ├── deployment/         # Deployment templates
    ├── frontend/           # Frontend templates
    └── notebooks/          # Notebook templates
```

#### Key Files

- **`init.py`**: Runs during project initialization to set up the project structure
- **`task_*.py`**: Define Angreal tasks that can be run with `angreal [task]`
- **`templates/`**: Contains template files that are used by tasks to generate new files

### `docs/` - Documentation

```
docs/
├── explanation/            # Explanatory documentation
│   ├── design-decisions.md # Design decisions explanation
│   ├── epoch-based-development.md # Explanation of epoch approach
│   └── index.md            # Explanation index
├── how-to/                 # How-to guides
│   ├── adding-epochs.md    # Guide for adding epochs
│   ├── creating-models.md  # Guide for creating models
│   ├── getting-started.md  # Getting started guide
│   └── index.md            # How-to index
├── reference/              # Reference documentation
│   ├── api/                # API reference
│   │   └── index.md        # API index
│   ├── command-reference.md # Command reference
│   ├── project-structure.md # Project structure reference
│   └── index.md            # Reference index
├── tutorials/              # Tutorials
│   └── getting-started.md  # Getting started tutorial
└── index.md                # Documentation home page
```

#### Key Files

- **`index.md`**: Main entry point for the documentation
- **`explanation/`**: In-depth explanations of concepts and design decisions
- **`how-to/`**: Task-oriented guides for specific use cases
- **`reference/`**: Technical reference material
- **`tutorials/`**: Step-by-step guides for beginners

### `notebooks/` - Jupyter Notebooks

```
notebooks/
├── README.md               # Notebook guidelines
├── epoch_001/              # First development/experimental phase
│   ├── README.md           # Epoch description
│   └── *.ipynb             # Notebooks for this epoch
├── epoch_00N/              # Nth development/experimental phase
│   ├── README.md           # Epoch description
│   └── *.ipynb             # Notebooks for this epoch
└── templates/              # Notebook templates
    └── notebook_template.ipynb  # Template for new notebooks
```

#### Key Files

- **`README.md`**: Guidelines for organizing and naming notebooks
- **`epoch_*/README.md`**: Description and purpose of each epoch
- **`templates/notebook_template.ipynb`**: Template for creating new notebooks

### `src/` - Source Code

```
src/
└── package_name/           # Main package
    ├── __init__.py         # Package initialization
    ├── api/                # API endpoints
    │   └── __init__.py
    ├── core/               # Core functionality
    │   ├── __init__.py
    │   ├── config.py       # Configuration definitions
    │   └── settings.py     # Settings management
    ├── data/               # Data loading and processing
    │   └── __init__.py
    ├── database/           # Database models (optional)
    │   ├── __init__.py
    │   ├── db.py           # Database connection utilities
    │   ├── migrations/     # Alembic migrations
    │   │   ├── __init__.py
    │   │   ├── env.py
    │   │   └── versions/
    │   │       └── __init__.py
    │   └── models/         # SQLAlchemy models
    │       ├── __init__.py
    │       ├── base.py     # Base model class
    │       ├── item.py     # Example item model
    │       └── user.py     # Example user model
    ├── models/             # Machine learning models
    │   └── __init__.py
    ├── pipelines/          # Data and training pipelines
    │   └── __init__.py
    ├── services/           # Business logic and services
    │   └── __init__.py
    ├── utils/              # Utility functions
    │   ├── __init__.py
    │   └── notebook.py     # Notebook utilities
    └── viz/                # Visualization components
        └── __init__.py
```

#### Key Files

- **`__init__.py`**: Package initialization, often contains version information
- **`core/config.py`**: Configuration definitions using Pydantic
- **`core/settings.py`**: Settings management and loading
- **`utils/notebook.py`**: Utilities for Jupyter notebooks
- **`database/models/base.py`**: Base model class for SQLAlchemy models

### `tests/` - Test Suite

```
tests/
├── README.md               # Testing guidelines
├── __init__.py
├── conftest.py             # Pytest configuration
├── functional/             # Functional tests
│   └── __init__.py
├── integration/            # Integration tests
│   └── __init__.py
└── unit/                   # Unit tests
    ├── __init__.py
    └── example_test.py     # Example test file
```

#### Key Files

- **`README.md`**: Guidelines for writing and organizing tests
- **`conftest.py`**: Pytest configuration and fixtures
- **`unit/example_test.py`**: Example test file with patterns to follow

### Optional Components

#### `frontend/` - Streamlit Dashboard

```
frontend/
├── README.md               # Frontend documentation
├── app.py                  # Main Streamlit application
└── requirements.txt        # Frontend-specific dependencies
```

#### Key Files

- **`README.md`**: Documentation for the frontend
- **`app.py`**: Main Streamlit application entry point
- **`requirements.txt`**: Frontend-specific dependencies

#### `deployment/` - Deployment Tools

```
deployment/
├── Dockerfile              # Docker configuration
├── app.sh                  # Application startup script
└── docker-compose.yml      # Docker Compose configuration
```

#### Key Files

- **`Dockerfile`**: Instructions for building a Docker image
- **`app.sh`**: Script for starting the application in a container
- **`docker-compose.yml`**: Configuration for multi-container applications

### Configuration Files

#### `.gitignore`

Specifies files and directories that should be ignored by Git, such as:

- Virtual environments
- Compiled Python files
- Notebook checkpoints
- Local configuration files
- Build artifacts

#### `.pre-commit-config.yaml`

Configures pre-commit hooks for code quality checks:

- Code formatting (e.g., ruff)
- Linting
- Type checking
- Security checks
- Custom checks

#### `mkdocs.yml`

Configures the MkDocs documentation system:

- Site structure and navigation
- Theme and appearance
- Extensions and plugins
- Markdown extensions

#### `pyproject.toml`

Defines the project metadata and dependencies:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "package_name"
version = {attr = "package_name.__version__"}
description = "Project description"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]

# Base dependencies
dependencies = [
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
    # ... other dependencies
]

# Optional dependency groups
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    # ... development dependencies
]
docs = [
    "mkdocs>=1.4.0",
    # ... documentation dependencies
]
notebooks = [
    "jupyter>=1.0.0",
    # ... notebook dependencies
]
```

## File Templates

The template includes several file templates that are used to generate new files:

### Notebook Template

```python
# Notebook Title
# Author: Your Name
# Date: YYYY-MM-DD
# Description: Brief description of notebook purpose and objectives

## Notebook Objectives
# - Objective 1
# - Objective 2
# - Objective 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Enable auto-reloading of modules
from package_name.utils.notebook import setup_notebook
setup_notebook()

# ... rest of the template
```

### Model Template

```python
"""
Model name model.
"""

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel


class ModelName(BaseModel):
    """
    Model description
    """
    __tablename__ = 'table_name'
    
    # Define your columns here:
    # name = Column(String, nullable=False)
    # description = Column(String)
    
    # Define relationships here (if needed):
    # items = relationship("RelatedModel", back_populates="related_attribute")
    
    def __repr__(self):
        return f"<ModelName(id={self.id})>"
```

### Epoch README Template

```markdown
# Epoch NNN: Description

## Overview

Brief description of this epoch's purpose and goals.

## Key Tasks

- Task 1
- Task 2
- Task 3

## Notebooks

List of notebooks in this epoch and their purposes.
```

## Environment Variables

The template uses environment variables for configuration. These are prefixed with the project's environment prefix (set during initialization) to avoid conflicts with other applications:

- `PREFIX_DATABASE_URL`: Database connection string
- `PREFIX_DEBUG`: Enable debug mode (true/false)
- `PREFIX_LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

Where `PREFIX` is the environment variable prefix set during project initialization.

## Package Organization Principles

The template follows several principles for organizing the Python package:

1. **Separation of concerns**: Each module has a clear responsibility
2. **Minimal dependencies**: Modules should have minimal dependencies on each other
3. **Progressive disclosure**: Simple interfaces with advanced options when needed
4. **Clear abstractions**: Well-defined interfaces between components
5. **Testability**: Design for easy testing

These principles help ensure that the code remains maintainable and adaptable as the project grows.

## Customization Points

The template is designed to be customized in several ways:

1. **Adding new modules**: Create new directories in `src/package_name/`
2. **Extending existing modules**: Add new files to existing modules
3. **Modifying templates**: Edit files in `.angreal/templates/`
4. **Adding new tasks**: Create new task files in `.angreal/`
5. **Changing configuration**: Modify `core/config.py` and `core/settings.py`

When customizing the template, try to follow the existing patterns and principles to maintain consistency and maintainability.
