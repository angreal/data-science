# Directory Structure

This page details the complete directory structure of the template and explains the purpose of each component.

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

The `.angreal` directory contains automation scripts and templates for project tasks. These tasks are defined using [Angreal](https://angreal.github.io/angreal/), a Python-based tool for project templating and task automation.

### `docs/` - Documentation

```
docs/
├── explanation/            # Explanatory documentation
├── how-to/                 # How-to guides
├── reference/              # Reference documentation
├── tutorials/              # Tutorials
└── index.md                # Documentation home page
```

The `docs` directory follows the [Diátaxis framework](https://diataxis.fr/) for technical documentation, which organizes documentation into four distinct categories: tutorials, how-to guides, explanation, and reference.

### `notebooks/` - Jupyter Notebooks

```
notebooks/
├── README.md               # Notebook guidelines
├── epoch_001/              # First development/experimental phase
│   ├── README.md           # Epoch description
│   └── *.ipynb             # Notebooks for this epoch
├── epoch_00N/              # Nth development/experimental phase
└── templates/              # Notebook templates
    └── notebook_template.ipynb  # Template for new notebooks
```

The `notebooks` directory organizes Jupyter notebooks into epochs, representing distinct phases of experimentation or development. Each epoch has its own directory and README describing its purpose and outcomes.

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
    │   ├── migrations/     # Alembic migrations
    │   └── models/         # SQLAlchemy models
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

The `src` directory contains the Python package with all reusable code. It follows a modular structure with clear separation of concerns.

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

The `tests` directory contains the test suite for the project, organized by test type (unit, integration, functional).

### Optional Components

#### `frontend/` - Streamlit Dashboard

```
frontend/
├── README.md               # Frontend documentation
├── app.py                  # Main Streamlit application
└── requirements.txt        # Frontend-specific dependencies
```

The `frontend` directory contains a Streamlit dashboard for visualizing data and model results. This component is optional and can be included during project initialization.

#### `deployment/` - Deployment Tools

```
deployment/
├── Dockerfile              # Docker configuration
├── app.sh                  # Application startup script
└── docker-compose.yml      # Docker Compose configuration
```

The `deployment` directory contains tools for deploying the project in production. This component is optional and can be included during project initialization.
