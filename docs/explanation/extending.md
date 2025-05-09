# Extending the Template

This document explains how to extend and customize the Data Science Template for your specific needs.

## Overview

The template is designed to be flexible and extensible. There are several ways to customize it:

1. **Modifying existing components**: Change how existing components work
2. **Adding new components**: Add entirely new functionality
3. **Removing components**: Remove components you don't need
4. **Changing workflows**: Modify how the template encourages you to work

This guide covers common customization patterns and provides examples.

## Customization Points

### Modifying Configuration

The simplest way to customize the template is to modify the configuration:

1. **Project metadata**: Edit `pyproject.toml` to change project name, description, and dependencies
2. **Documentation**: Edit `mkdocs.yml` to change documentation structure and appearance
3. **Environment variables**: Edit `.env` files to change runtime configuration
4. **Settings**: Edit `src/package_name/core/config.py` to change application settings

### Adding New Modules

To add a new module to your package:

1. Create a new directory in `src/package_name/`
2. Add an `__init__.py` file
3. Add your module code
4. Update imports as needed

For example, to add a module for monitoring:

```
src/package_name/monitoring/
├── __init__.py
├── alerts.py
└── metrics.py
```

### Extending Command Line Tasks

The template uses Angreal for task automation. To add a new task:

1. Create a new file `.angreal/task_your_task.py`
2. Define your task using the Angreal API
3. Implement the task functionality

Example:

```python
# task_report.py
import angreal

@angreal.command(name='report', about='Generate a project report')
@angreal.argument(name='output', help='Output file path')
def report(output):
    """Generate a project report."""
    # Your code here
    print(f"Generated report at {output}")
```

### Customizing Notebook Templates

To customize the notebook template:

1. Edit `.angreal/templates/notebooks/notebook_template.ipynb`
2. Adjust the structure, imports, or standard cells
3. Add custom styling or setup code

### Adding Frontend Components

If you're using the frontend option, you can extend it by:

1. Adding new pages to `frontend/`
2. Creating reusable components
3. Adding custom visualizations
4. Integrating with your data and models

### Extending Database Models

If you're using the database option, you can extend it by:

1. Adding new models to `src/package_name/database/models/`
2. Creating relationships between models
3. Adding database utilities
4. Creating migrations for schema changes

## Common Extension Patterns

### Adding Experiment Tracking

To add experiment tracking with MLflow:

1. Add MLflow to your dependencies in `pyproject.toml`
2. Create a new module `src/package_name/tracking/`
3. Add utilities for experiment logging and management
4. Integrate with your training code

### Adding Data Versioning

To add data versioning with DVC:

1. Initialize DVC in your project
2. Add data files to DVC tracking
3. Create a data pipeline using DVC
4. Document the data versioning workflow

### Adding CI/CD Integration

To add CI/CD integration:

1. Create configuration files for your CI/CD platform (e.g., GitHub Actions, GitLab CI)
2. Set up testing, linting, and documentation workflows
3. Configure deployment pipelines
4. Add badges and status indicators to your README

### Adding Model Registry

To add a model registry:

1. Create a new module `src/package_name/registry/`
2. Add utilities for model versioning and management
3. Integrate with your training and deployment code
4. Document the model registry workflow

## Best Practices for Extensions

1. **Follow the existing patterns**: Try to match the style and organization of the existing code
2. **Document your extensions**: Add documentation for your extensions
3. **Write tests**: Add tests for your extensions
4. **Keep it modular**: Design extensions to be loosely coupled with existing code
5. **Update dependencies**: Keep dependencies up to date in `pyproject.toml`
6. **Consider sharing**: If your extension would be useful to others, consider contributing it back

## Examples

### Example: Adding a New Task

```python
# task_explore.py
import angreal
import os
import pandas as pd
import webbrowser

@angreal.command(name='explore', about='Explore a dataset with pandas-profiling')
@angreal.argument(name='dataset', help='Path to the dataset')
@angreal.argument(name='output', help='Output file path', required=False)
def explore(dataset, output=None):
    """Explore a dataset with pandas-profiling."""
    from pandas_profiling import ProfileReport
    
    print(f"Loading dataset from {dataset}...")
    df = pd.read_csv(dataset)
    
    print(f"Generating profile report...")
    profile = ProfileReport(df, title="Dataset Profiling Report")
    
    if output:
        output_path = output
    else:
        output_path = os.path.join("reports", "profile.html")
        os.makedirs("reports", exist_ok=True)
    
    profile.to_file(output_path)
    print(f"Report generated at {output_path}")
    
    # Open the report in a browser
    webbrowser.open(f"file://{os.path.abspath(output_path)}")
```

### Example: Customizing Configuration

```python
# config.py
from pydantic import BaseModel, Field

class AppSettings(BaseModel):
    # ... existing settings ...
    
    # Add new settings
    model_registry_path: str = Field(
        default="./models",
        description="Path to the model registry"
    )
    
    experiment_tracking_uri: str = Field(
        default="sqlite:///mlflow.db",
        description="URI for MLflow tracking"
    )
    
    max_workers: int = Field(
        default=4,
        description="Maximum number of parallel workers"
    )
```

### Example: Adding a New Module

```python
# src/package_name/tracking/__init__.py
"""Experiment tracking module."""

from .mlflow import log_experiment, load_experiment

__all__ = ["log_experiment", "load_experiment"]
```

```python
# src/package_name/tracking/mlflow.py
"""MLflow integration for experiment tracking."""

import mlflow
from ..core.settings import get_settings

settings = get_settings()

def setup_tracking():
    """Set up MLflow tracking."""
    mlflow.set_tracking_uri(settings.experiment_tracking_uri)

def log_experiment(name, params, metrics, artifacts=None):
    """Log an experiment to MLflow."""
    setup_tracking()
    
    with mlflow.start_run(run_name=name):
        # Log parameters
        for key, value in params.items():
            mlflow.log_param(key, value)
        
        # Log metrics
        for key, value in metrics.items():
            mlflow.log_metric(key, value)
        
        # Log artifacts
        if artifacts:
            for artifact_path in artifacts:
                mlflow.log_artifact(artifact_path)
    
    return mlflow.active_run().info.run_id

def load_experiment(run_id):
    """Load an experiment from MLflow."""
    setup_tracking()
    return mlflow.get_run(run_id)
```

## Conclusion

The Data Science Template is designed to be a starting point, not a limitation. By understanding the customization points and extension patterns, you can adapt it to fit your specific needs while maintaining the benefits of the structured approach.

Remember that the goal is to enhance your productivity and the maintainability of your project. Customize the template in ways that support these goals, and don't be afraid to experiment with different approaches.
