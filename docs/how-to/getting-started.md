# Getting Started

This guide will help you get started with the Data Science Template, from installation to creating your first project.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- [Angreal](https://angreal.github.io/angreal/) for template rendering

## Installation

### Install Angreal

First, install Angreal if you haven't already:

```bash
pip install angreal
```

### Initialize a New Project

To create a new project using this template:

```bash
angreal init https://github.com/yourusername/data-science-template.git
```

### Follow the Interactive Prompts

The initialization process will prompt you with several questions to configure your project:

```
What is the name of your project?
What would you like the project slug for your project to be?
What would you like the name of your python package to be?
Can you give a short (1-2 sentence) description of your project?
What would you like the environment variable prefix for your project to be?
Would you like to include database support with migrations? (true/false)
Would you like to include a Streamlit frontend? (true/false)
Would you like to include application deployment scripts? (true/false)
```

Answer these questions according to your project requirements.

## Project Setup

After initializing your project, navigate to the project directory:

```bash
cd your-project-slug
```

### Create a Virtual Environment

It's recommended to use a virtual environment for your project:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### Install Dependencies

Install the project and its dependencies:

```bash
# Install the base project
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

# Install documentation dependencies
pip install -e ".[docs]"

# Install notebook dependencies
pip install -e ".[notebooks]"

# Install all dependencies
pip install -e ".[all]"
```

Choose the installation options based on your project needs.

### Initialize Git Repository

If you want to use version control (recommended):

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial project setup from template"
```

## First Steps

After setting up your project, here are some recommended first steps:

### 1. Update README

Update the main README.md with your project-specific information:

- Project name and description
- Installation instructions
- Usage examples
- Team information

### 2. Create Your First Epoch

Create your first epoch for exploratory analysis:

```bash
angreal new epoch --description "Initial exploration and data analysis"
```

### 3. Create Your First Notebook

Create a notebook in your first epoch:

```bash
angreal new notebook --title "Data Exploration" --author "Your Name"
```

### 4. Explore the Project Structure

Take some time to explore the project structure and familiarize yourself with the different components:

- `src/`: Source code package
- `notebooks/`: Jupyter notebooks
- `docs/`: Documentation
- `tests/`: Test suite

### 5. Build Documentation

Build and view the project documentation:

```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

Open your browser and navigate to http://127.0.0.1:8000/ to view the documentation.

### 6. Set Up Pre-commit Hooks

To ensure code quality, set up pre-commit hooks:

```bash
# Install pre-commit
pip install pre-commit

# Install pre-commit hooks
pre-commit install
```

## Next Steps

After completing these initial steps, consider the following next steps:

1. **Define your data sources**: Identify where your data will come from and how to access it
2. **Create data loading utilities**: Implement functions for loading and processing your data
3. **Develop exploratory analyses**: Use notebooks to explore your data and develop initial insights
4. **Refactor code into modules**: Move reusable code from notebooks to your package
5. **Write tests**: Develop tests for your core functionality
6. **Build documentation**: Document your project, its components, and your findings

Refer to the other how-to guides for more detailed instructions on specific tasks.
