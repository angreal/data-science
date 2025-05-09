# {{ project_name }}

{{ project_desc_short }}

## Project Overview

This project was created using a data science project template with a focus on maintainability, reproducibility, and best practices.

## Features

- **Modular Project Structure**: Organized layout for code, notebooks, documentation, and tests
- **Epoch-Based Notebook Organization**: Track your experimental progress over time
- **Domain-Specific Components**: Dedicated modules for data processing, models, visualizations, etc.
- **Customizable Infrastructure**:
  - **Database Support**: SQLAlchemy with Alembic migrations
  - **Frontend Dashboard**: Streamlit application for data visualization
  - **Deployment Tools**: Docker and deployment scripts for production

## Project Structure

```
{{ project_slug }}/
├── docs/                   # Documentation
├── notebooks/              # Jupyter notebooks organized by epochs
│   ├── epoch_001/          # Experiment phases
│   └── README.md           # Notebook guidelines
├── src/                    # Source code
│   └── {{ package_name }}/       # Main package
│       ├── core/           # Core functionality and configuration
│       ├── data/           # Data loading, processing, and feature engineering
│       ├── database/       # Database models and connections (optional)
│       ├── models/         # ML model definitions, training and evaluation
│       ├── pipelines/      # Data and modeling workflows
│       └── utils/          # Utility functions and helpers
├── tests/                  # Test suite
├── app.sh                  # Application Launcher
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project overview
```

## Code Organization

This project follows a domain-driven structure to organize code by functionality:

### Data Processing (`{{ package_name }}.data`)
Contains all data-related operations:
- Data loading and ingestion
- Data cleaning and preprocessing
- Feature engineering
- Dataset creation and management

### Models (`{{ package_name }}.models`)
Contains machine learning model implementations:
- Model architectures
- Training procedures
- Evaluation metrics and methods
- Inference utilities

### Pipelines (`{{ package_name }}.pipelines`)
Contains end-to-end workflows:
- Data processing pipelines
- Training pipelines
- Evaluation pipelines
- Deployment pipelines

### Services (`{{ package_name }}.services`)
Contains business logic and application services:
- Prediction services
- Scheduling
- Monitoring
- External service clients

### API (`{{ package_name }}.api`)
Contains API definitions (if applicable):
- API endpoints
- Request/response models
- API dependencies and middleware

### Visualization (`{{ package_name }}.viz`)
Contains visualization components:
- Plotting utilities
- Dashboard components
- Exploratory visualizations
- Model interpretability visualizations

### Core (`{{ package_name }}.core`)
Contains core application functionality:
- Configuration management
- Logging setup
- Common exceptions
- Base classes

### Utils (`{{ package_name }}.utils`)
Contains general utility functions:
- Helper functions
- Decorators
- Custom types
- Miscellaneous tools

### Database (`{{ package_name }}.database`)
Contains database models and utilities (if enabled):
- SQLAlchemy models
- Database connection management
- Migrations

## Installation

### Development Environment

```bash
# Clone the repository
git clone [repository-url]
cd {{ project_slug }}

# Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package with development dependencies
pip install -e '.[dev]'
```

### Other Installation Options

```bash
# Basic installation
pip install -e '.'

# Install with specific components
pip install -e '.[notebooks]'  # For notebook dependencies
pip install -e '.[docs]'       # For documentation tools
pip install -e '.[app]'        # For deployment tools

# Full installation with all dependencies
pip install -e '.[all]'
```

## Getting Started

### Working with Notebooks

Notebooks are organized in epoch folders to track the evolution of your analysis:

```bash
# Navigate to notebooks directory
cd notebooks/epoch_001/

# Start Jupyter
jupyter lab
```

### Creating New Epochs

If you've set up the project with angreal, create new epochs with:

```bash
angreal new epoch --description "Description of this experimental phase"
```

### Creating New Notebooks

Create a new notebook with:

```bash
angreal new notebook --title "Analysis Title" --author "Your Name"
```

## Configuration System

This project uses a robust configuration system that allows you to manage settings across different environments and sources.

### Overview

The configuration system consists of two main components:

1. **Configuration Definition** (`core/config.py`) - Defines the schema and default values for all settings
2. **Configuration Management** (`core/settings.py`) - Handles loading settings from various sources and providing access

### How It Works

Settings are loaded in order of precedence:

1. **Direct overrides** (highest precedence) - Values passed directly to `get_settings()`
2. **Environment variables** - Variables with the prefix `{{ environment_prefix }}`
3. **.env file values** - Key-value pairs in `.env` files with the prefix `{{ environment_prefix }}`
4. **Default values** (lowest precedence) - Defined in the `AppSettings` class

### Using the Configuration

To access settings in your code:

```python
from {{ package_name }}.core.settings import get_settings

# Get settings with defaults
settings = get_settings()
print(settings.database_url)  # "sqlite:///app.db"

# Override settings for testing
test_settings = get_settings(database_url="sqlite:///test.db")
print(test_settings.database_url)  # "sqlite:///test.db"

# Use a specific .env file
prod_settings = get_settings(env_file=".env.production")
```

### Adding New Settings

To add new settings to your application:

1. Open `core/config.py`
2. Add new fields to the `AppSettings` class with type hints and defaults:

```python
class AppSettings(BaseModel):
    # Existing settings...
    
    # New settings
    api_key: Optional[str] = Field(
        default=None,
        description="API key for external service"
    )
    worker_count: int = Field(
        default=4,
        description="Number of worker processes"
    )
```

### Environment Variables

You can override settings using environment variables:

```bash
export {{ environment_prefix }}DATABASE_URL="postgresql://user:pass@localhost/db"
export {{ environment_prefix }}DEBUG=true
export {{ environment_prefix }}LOG_LEVEL=DEBUG
```

### Configuration Files

Create a `.env` file in your project root:

```
{{ environment_prefix }}DATABASE_URL=postgresql://user:pass@localhost/db
{{ environment_prefix }}DEBUG=true
{{ environment_prefix }}LOG_LEVEL=DEBUG
```

For different environments, create different files:
- `.env.development`
- `.env.testing`
- `.env.production`

## Database Models

If you've enabled database support, you can create new models using the angreal command:

```bash
angreal new-model UserProfile --description "User profile information" --table_name "user_profiles"
```

This will create a new model file in `src/{{ package_name }}/database/models/` and update the imports automatically.

## Testing

This project uses a comprehensive testing approach with a directory structure that mirrors the source code organization.

### Test Types

- **Unit Tests**: Test individual functions and classes in isolation
- **Integration Tests**: Test how components work together
- **Functional Tests**: End-to-end tests that verify entire workflows

### Directory Structure

Tests are organized to mirror the source code structure:

```
tests/
├── conftest.py        # Shared pytest fixtures and configuration
├── functional/        # End-to-end functional tests
├── integration/       # Integration tests between components
└── unit/              # Unit tests mirroring src structure
```

For unit tests, create test files that mirror the structure of the `src` directory. For example:

- For `src/data/loading.py`, create `tests/unit/data/test_loading.py`
- For `src/models/train.py`, create `tests/unit/models/test_train.py`

### Running Tests

You can run tests using the provided Angreal task:

```bash
# Run unit tests (default)
angreal test

# Run specific test types
angreal test --unit
angreal test --integration
angreal test --functional

# Run notebook tests
angreal test --notebooks

# Run notebook tests for a specific epoch
angreal test --notebooks --epoch 001

# Run all tests
angreal test --all
```

Note: Notebook tests only check that notebooks execute without errors and do not compare outputs (for security reasons).

### Testing Best Practices

1. **Write Tests Early**: Follow test-driven development principles where possible
2. **Test Coverage**: Aim for high test coverage, especially for critical components
3. **Small, Focused Tests**: Each test should focus on a specific functionality
4. **Use Fixtures**: Use pytest fixtures for reusable test components
5. **Mock External Dependencies**: Use mocking to isolate tests from external systems
6. **Consistent Naming**: Follow a consistent naming pattern for test files and functions

### Code Migration Path

The recommended workflow for code in this project:

1. **Exploration**: Initial exploration and experimentation in notebooks
2. **Extraction**: Extract reusable code into appropriate modules
3. **Testing**: Write tests for the extracted code
4. **Refinement**: Refine the implementation based on test results
5. **Documentation**: Update notebooks to use the refined implementation

## Documentation

This project includes a pre-configured documentation system using MkDocs with the Material theme, following the Diátaxis framework.

### Building Documentation

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Serve documentation locally
angreal docs serve

# Build static site
angreal docs build
```

Documentation will be built in the `site/` directory (which is git-ignored).

### Documentation Structure

The documentation follows the [Diátaxis framework](https://diataxis.fr/) with four types of documentation:

- `docs/tutorials/`: Learning-oriented content to help users get started
- `docs/how-to/`: Problem-oriented guides for accomplishing specific tasks
- `docs/reference/`: Information-oriented technical reference material
- `docs/explanation/`: Understanding-oriented conceptual explanations

## Deployment

If you've enabled deployment tools, you can deploy the application with:

```bash
cd deployment
docker-compose up -d
```

## License

[Choose an appropriate license]

## Contact

[Your contact information]
