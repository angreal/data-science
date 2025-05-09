# Core Components

This page describes the core components of the template that are always included regardless of optional features.

## Source Code Package

The heart of the template is the Python package in the `src/` directory. This package contains all reusable code that evolves from exploratory work in notebooks. The package is organized into several modules:

### Core Module

The `core` module contains fundamental functionality for the project:

```python
src/package_name/core/
├── __init__.py
├── config.py       # Configuration definitions using Pydantic
└── settings.py     # Settings management with environment variables
```

#### Configuration System

The configuration system uses Pydantic to define a type-safe configuration schema:

```python
# config.py
from pydantic import BaseModel, Field

class AppSettings(BaseModel):
    """Application configuration structure."""
    
    database_url: str = Field(
        default="sqlite:///app.db",
        description="Database connection string"
    )
    
    debug: bool = Field(
        default=False,
        description="Enable debug mode"
    )
```

#### Settings Management

The settings management system loads configuration from various sources in order of precedence:

1. Direct overrides
2. Environment variables
3. `.env` file values
4. Default values

```python
# settings.py (simplified)
def get_settings(**kwargs):
    """Get settings instance with configuration."""
    return Settings.get_instance(**kwargs)
```

### Utils Module

The `utils` module contains utility functions used throughout the project:

```python
src/package_name/utils/
├── __init__.py
└── notebook.py     # Notebook utilities
```

#### Notebook Utilities

The template includes utilities for working with Jupyter notebooks, such as setting up autoreload and path configuration:

```python
# notebook.py (simplified)
def setup_notebook(autoreload=True):
    """Set up a Jupyter notebook with common configurations."""
    # Enable autoreload if requested
    # Add project root to Python path
```

### Data Module

The `data` module is for data loading, processing, and feature engineering:

```python
src/package_name/data/
└── __init__.py
```

This module is intentionally minimal in the template, allowing you to structure your data processing code according to your project's needs.

### Models Module

The `models` module is for machine learning models:

```python
src/package_name/models/
└── __init__.py
```

Like the data module, this is intentionally minimal in the template, allowing you to organize your models as appropriate for your project.

### Pipelines Module

The `pipelines` module is for data and training pipelines:

```python
src/package_name/pipelines/
└── __init__.py
```

This module is intended for creating reproducible pipelines that connect data processing, feature engineering, and model training.

### Visualization Module

The `viz` module is for reusable visualization components:

```python
src/package_name/viz/
└── __init__.py
```

This module is for visualization code that is used across notebooks or in the frontend.

## Notebook Organization

The template uses an epoch-based approach to organize notebooks:

```
notebooks/
├── README.md
├── epoch_001/
│   ├── README.md
│   └── *.ipynb
└── templates/
    └── notebook_template.ipynb
```

### Epochs

Epochs represent distinct phases of experimentation or development. Each epoch has its own directory with a README describing its purpose and outcomes. This approach helps track the evolution of your project over time.

### Notebook Template

The template includes a standardized notebook template with sections for:

1. Metadata (title, author, date, description)
2. Objectives
3. Approach
4. Configuration
5. Data loading
6. Analysis
7. Results and visualization
8. Findings and conclusions

This structure encourages good documentation practices and makes notebooks more readable and reproducible.

## Documentation System

The template includes a comprehensive documentation system using MkDocs:

```
docs/
├── explanation/
├── how-to/
├── reference/
├── tutorials/
└── index.md
```

### Diátaxis Framework

The documentation follows the [Diátaxis framework](https://diataxis.fr/), which organizes documentation into four distinct categories:

1. **Tutorials**: Learning-oriented content for beginners
2. **How-to Guides**: Task-oriented instructions for solving specific problems
3. **Explanation**: Understanding-oriented discussions of concepts
4. **Reference**: Information-oriented technical descriptions

This approach ensures that documentation serves different user needs effectively.

## Testing Infrastructure

The template includes a structured testing approach:

```
tests/
├── README.md
├── __init__.py
├── conftest.py
├── functional/
├── integration/
└── unit/
```

### Test Types

Tests are organized by type:

1. **Unit Tests**: Test individual functions or classes in isolation
2. **Integration Tests**: Test how components work together
3. **Functional Tests**: Test complete features or user flows

### Pytest Configuration

The template includes a basic pytest configuration in `conftest.py` for setting up test fixtures and other test-wide configurations.

## Project Configuration

The template uses modern Python project configuration:

```python
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{{ package_name }}"
version = {attr = "{{ package_name }}.__version__"}
# ...dependencies and other metadata
```

### Optional Dependencies

The project configuration includes optional dependency groups:

```python
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.2.0",
]

docs = [
    "mkdocs>=1.4.0",
    "mkdocs-material>=8.5.0",
    # ...
]

notebooks = [
    "jupyter>=1.0.0",
    "matplotlib>=3.7.0",
    # ...
]

app = [
    "docker>=6.1.0",
    "gunicorn>=21.0.0",
]

all = [
    "{{ package_name }}[dev]",
    "{{ package_name }}[docs]",
    "{{ package_name }}[notebooks]",
    "{{ package_name }}[app]",
]
```

This structure allows users to install only the dependencies they need for specific tasks.
