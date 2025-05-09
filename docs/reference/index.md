# Reference

This section provides detailed technical reference for the Data Science Template's components, APIs, and configuration options.

## Contents

- [Project Structure](project-structure.md): Detailed reference for the complete project structure
- [Command Reference](command-reference.md): Reference for all template commands
- [Utility Functions](utility-functions.md): Reference for utility functions (coming soon)
- [Template Variables](template-variables.md): Reference for template variables (coming soon)

## What is Reference Documentation?

Reference documentation provides detailed, authoritative information about the technical aspects of the template. It's designed for looking up specific information rather than learning concepts or completing tasks.

### When to Use This Section

- When you need detailed information about a specific component
- When you need to look up command options or arguments
- When you need to understand the structure and organization of the template
- When you need to know what configuration options are available

## Key References

### Project Structure

The template creates a structured directory layout for your project:

```
project_name/
├── .angreal/               # Project tasks and automation
├── docs/                   # Documentation
├── notebooks/              # Jupyter notebooks organized by epochs
├── src/                    # Source code
├── tests/                  # Test suite
├── frontend/               # Streamlit dashboard (optional)
├── deployment/             # Deployment scripts (optional)
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # Project overview
```

See the [Project Structure](project-structure.md) reference for a complete breakdown.

### Commands

The template provides several commands through the Angreal task system:

- `angreal new epoch`: Create a new epoch directory
- `angreal new notebook`: Create a new notebook from a template
- `angreal test`: Run the test suite
- `angreal docs`: Build and serve documentation

See the [Command Reference](command-reference.md) for a complete list.

### Configuration

The template uses several configuration files:

- `pyproject.toml`: Project metadata and dependencies
- `mkdocs.yml`: Documentation configuration
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `src/package_name/core/config.py`: Application configuration

### Environment Variables

The template uses environment variables for configuration, prefixed with your project's environment prefix:

- `PREFIX_DATABASE_URL`: Database connection string
- `PREFIX_DEBUG`: Enable debug mode (true/false)
- `PREFIX_LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

## API Documentation

For detailed API documentation, refer to the specific reference pages. These pages are generated from docstrings in the code and provide complete information about functions, classes, and modules.

## Further Reading

For more information about specific topics, refer to the explanatory documentation:

- [Design Decisions](../explanation/design-decisions.md): Explains the key design decisions
- [Epoch-Based Development](../explanation/epoch-based-development.md): Explains the epoch concept
- [Extending the Template](../explanation/extending.md): Guide to customizing the template
