# Modern Data Science Project Template
---

A modern Python template for data science projects with epoch-based notebook organization and scientific computing patterns.

## Features

- **Epoch-based Development**: Organize notebooks chronologically with `angreal new epoch`
- **Scientific Computing Stack**: Jupyter, matplotlib, seaborn, and testing with nbval
- **Modern Configuration**: Pydantic-based settings with environment variable support
- **Code Quality**: Ruff linting, mypy type checking, pytest testing
- **Notebook Utilities**: Automatic project setup and IPython configuration

## Usage

### Initial Setup

```bash
pip install angreal
angreal init /path/to/this/template
cd your-project
pip install -e '.[dev,notebooks]'  # Install with development and notebook dependencies
```

### Epoch-based Development

Create a new exploration epoch:
```bash
angreal new epoch --description "Initial data exploration"
```

Create a notebook in the current epoch:
```bash
angreal new notebook --title "Data Loading and Cleaning" --author "Your Name"
```

### Project Structure

```
your-project/
├── src/your_package/
│   ├── core/           # Configuration and settings
│   └── utils/          # Notebook utilities and helpers
├── notebooks/          # Epoch-organized notebooks
│   └── epoch_001/      # Auto-created epoch directories
├── tests/              # Unit and integration tests
└── pyproject.toml      # Modern Python packaging
```

