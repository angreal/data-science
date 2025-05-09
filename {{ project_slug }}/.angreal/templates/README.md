# Template Files

This directory contains template files used by the data science project template.

## Directory Structure

- `database/`: Templates for SQLAlchemy database integration
  - `__init__.py`: Package initialization
  - `models.py`: SQLAlchemy model definitions
  - `db.py`: Database connection utilities
  - `migrations/`: Alembic migration templates
  - `alembic.ini`: Alembic configuration

- `frontend/`: Templates for Streamlit dashboard
  - `app.py`: Main Streamlit application
  - `requirements.txt`: Frontend dependencies
  - `README.md`: Frontend documentation

- `deployment/`: Templates for deployment
  - `Dockerfile`: Container definition
  - `docker-compose.yml`: Service orchestration
  - `app.sh`: Deployment script

- `notebooks/`: Templates for notebook creation
  - `notebook_template.ipynb`: Base notebook structure
  - `epoch_readme.md`: README template for new epochs

## Template Variables

These templates use the following variables:

- `project_name`: Full project name
- `project_slug`: URL-friendly version of the project name
- `package_name`: Python package name (derived from project_slug)
- `project_desc_short`: Brief project description
- `environment_prefix`: Prefix for environment variables

Variables used at runtime by tasks (not during template rendering):
- notebook_title: Title for a new notebook
- notebook_author: Author of a notebook
- notebook_date: Creation date of a notebook
- epoch_number: Number of the current epoch
- epoch_description: Description of an epoch

## Usage

These templates are used by the task commands defined in:

- `init.py`: Used during project initialization
- `task_new.py`: Used for creating new epochs and notebooks

## Adding New Templates

To add new templates:

1. Create a new directory under `templates/` for your component
2. Add your template files with appropriate variable placeholders
3. Update the relevant task files to use your templates
