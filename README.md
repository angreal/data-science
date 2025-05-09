# Data Science Project Template

A comprehensive, customizable template for data science projects that follows best practices for project organization, development workflow, and deployment.

## Features

- **Modular Project Structure**: Organized layout for code, notebooks, documentation, and tests
- **Epoch-Based Notebook Organization**: Track your experimental progress over time
- **Comprehensive Documentation**: Detailed guides, explanations, and references
- **Testing Infrastructure**: Pre-configured for unit, integration, and functional tests
- **Optional Components**:
  - **Database Support**: SQLAlchemy with Alembic migrations
  - **Frontend Dashboard**: Streamlit application for data visualization
  - **Deployment Tools**: Docker and deployment scripts for production

## Getting Started

### Prerequisites

- Python 3.8+
- [Angreal](https://angreal.github.io/angreal/) for template rendering

### Installation

1. Install Angreal if you haven't already:

```bash
pip install angreal
```

2. Initialize a new project using this template:

```bash
angreal init https://github.com/yourusername/data-science-template.git
```

3. Follow the interactive prompts to configure your project.

## Documentation

This template includes comprehensive documentation:

- **Architecture**: Detailed explanation of the template's architecture and design decisions
- **How-To Guides**: Step-by-step guides for common tasks
- **Explanations**: In-depth explanations of concepts like epoch-based development
- **Reference**: Command reference, project structure, and API details

To view the documentation:

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build and serve documentation
mkdocs serve
```

Then open your browser to http://localhost:8000/

## Project Structure

```
project_name/
├── .angreal/               # Project tasks and automation
├── docs/                   # Documentation
├── notebooks/              # Jupyter notebooks organized by epochs
│   ├── epoch_001/          # Experiment phases
│   └── README.md           # Notebook guidelines
├── src/                    # Source code
│   └── package_name/       # Main package
│       ├── core/           # Core functionality
│       ├── utils/          # Utility functions
│       └── database/       # Database models (optional)
├── tests/                  # Test suite
├── frontend/               # Streamlit dashboard (optional)
├── deployment/             # Deployment scripts (optional)
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project overview
```

For a detailed breakdown of the structure, see the [Project Structure Reference](docs/reference/project-structure.md).

## Command Reference

This template provides several custom commands to streamline your workflow:

### Creating New Epochs

Start a new experimental phase with:

```bash
angreal new epoch --description "Brief description of this phase"
```

This creates a new epoch directory in the notebooks folder with incrementing numbers (e.g., `epoch_002/`).

### Creating New Notebooks

Create a new notebook in the current (or specified) epoch:

```bash
angreal new notebook --title "Exploratory Data Analysis" --author "Your Name"
```

Optional parameters:
- `--epoch`: Specify which epoch to create the notebook in (e.g., "001")

For a complete list of commands, see the [Command Reference](docs/reference/command-reference.md).

## Optional Components

During project initialization, you can choose to include these optional components.

### Database Support

If enabled, this adds:
- SQLAlchemy models in `src/package_name/database/`
- Alembic migrations setup
- Database connection utilities

### Frontend Dashboard

If enabled, this adds:
- Streamlit application in the `frontend/` directory
- Sample dashboard with multiple pages

### Deployment Tools

If enabled, this adds:
- Dockerfile for containerization
- docker-compose.yml for orchestration
- Deployment script (`app.sh`)

## Installation Options

The template provides several installation options:

```bash
# Install base package
pip install -e .

# Install development tools (testing, linting)
pip install -e '.[dev]'

# Install documentation tools
pip install -e '.[docs]'

# Install notebook support
pip install -e '.[notebooks]'

# Install deployment tools
pip install -e '.[app]'

# Install all optional components
pip install -e '.[all]'
```

## Best Practices

This template encourages data science best practices:

1. **Experiment Tracking**: Organize notebooks by epochs to track experimental progress
2. **Code Reusability**: Move reusable code from notebooks to the package
3. **Documentation**: Document decisions, experiments, and code
4. **Modular Development**: Separate concerns into distinct modules
5. **Testing**: Write tests for core functionality
6. **Reproducibility**: Track dependencies and environment settings

For more details on how to implement these practices, see the [documentation](docs/index.md).

## Customization

You can customize this template by:

1. Modifying `angreal.toml` to change default values or add new options
2. Editing template files in `.angreal/templates/`
3. Adding new commands to `.angreal/task_*.py` files

See [Extending the Template](docs/explanation/extending.md) for more details.

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
