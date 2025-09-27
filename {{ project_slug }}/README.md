# {{ project_name }}

{{ project_short_description }}

A data science project using epoch-based development workflow for organized exploration and analysis.

## Quick Start

### Installation

```bash
# Install with development dependencies
pip install -e '.[dev]'

# Install with notebook support
pip install -e '.[notebooks]'

# Install everything
pip install -e '.[all]'
```

### Epoch-based Development

This project uses an epoch-based workflow to organize exploration chronologically:

#### Working with Epochs

The project starts with `epoch_001/` ready for your initial exploration. Create additional epochs with:

```bash
angreal new epoch --description "Feature engineering phase"
```

This creates a new `epoch_002/` directory in `notebooks/` with a structured README template.

#### Create a Notebook
```bash
angreal new notebook --title "Data Loading and Cleaning" --author "Your Name"
```

This creates a timestamped notebook (e.g., `2023-10-15_yn_data_loading_and_cleaning.ipynb`) in the current epoch with:
- Standardized header with title, author, date, and epoch
- Pre-configured imports and project setup
- Automatic IPython autoreload and path configuration

### Project Structure

```
{{ project_slug }}/
├── src/{{ package_name }}/
│   ├── core/                    # Configuration and settings
│   │   ├── config.py           # Pydantic configuration models
│   │   └── settings.py         # Settings management with env vars
│   ├── utils/                  # Shared utilities
│   │   └── notebook.py         # Jupyter notebook setup helpers
│   ├── __init__.py
│   └── __main__.py
├── notebooks/                  # Epoch-organized notebooks
│   ├── epoch_001/             # First exploration epoch
│   │   ├── README.md          # Epoch documentation
│   │   └── *.ipynb            # Dated notebooks
│   └── epoch_002/             # Subsequent epochs...
├── tests/                      # Test suites
│   ├── unit/                  # Unit tests
│   └── integration/           # Integration tests
└── pyproject.toml             # Project configuration
```

### Configuration Management

The project includes type-safe configuration using Pydantic:

```python
from {{ package_name }}.core.settings import get_settings

# Load settings from environment variables and .env file
settings = get_settings()
print(settings.log_level)  # INFO (default)

# Override settings
settings = get_settings(log_level='DEBUG')
```

Environment variables use the `{{ environment_prefix }}` prefix:
- `{{ environment_prefix }}LOG_LEVEL=DEBUG`

### Notebook Development

Each notebook automatically includes project setup:

```python
# This is included in the notebook template
from {{ package_name }}.utils.notebook import setup_notebook

# Enables autoreload and adds project to Python path
setup_notebook()

# Now you can import your project modules
import {{ package_name }}
```

### Development Commands

```bash
# Run tests
angreal task tests

# Run linting
angreal task lint

# Start development environment
angreal task dev
```

### Epoch Workflow Best Practices

1. **Start each major exploration phase with a new epoch**
   - Data collection and initial exploration
   - Feature engineering and preprocessing  
   - Model development and evaluation
   - Final analysis and reporting

2. **Document findings in each epoch's README**
   - Update the notebook table with descriptions
   - Record key findings and insights
   - Note next steps for future epochs

3. **Use descriptive notebook titles**
   - Focus on the specific analysis or task
   - Include key methodology or approach
   - Examples: "EDA Customer Segments", "Feature Engineering v2", "Model Comparison Random Forest vs XGBoost"

4. **Commit regularly within epochs**
   - After completing each notebook analysis
   - When reaching significant milestones
   - Before starting new experimental directions

This project was generated using a modern data science template with epoch-based workflow patterns.
