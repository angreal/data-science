# Notebook Templates

This directory contains templates for Jupyter notebooks that follow project standards.

## Available Templates

- `notebook_template.ipynb` - Standard notebook template with recommended structure and imports

## Using Templates

### Manual Approach

1. Copy the template to your working directory (e.g., `epoch_003/`)
2. Rename the template following the project naming convention:
   ```
   YYYY-MM-DD_author_initials_short_descriptive_name.ipynb
   ```
3. Update the metadata section with your name, date, and description
4. Uncomment and customize the imports as needed

### Using Angreal

You can create a new notebook using Angreal:

```bash
angreal new notebook --title "Analysis Title" --author "Your Name"
```

## Template Structure

The standard notebook template includes:

1. **Metadata Header** - Title, author, date, description, and objectives
2. **Standard Imports** - Common libraries and project-specific modules
3. **Configuration** - Parameters and settings for the notebook
4. **Data Loading** - Code for loading and preparing data
5. **Exploratory Analysis** - Initial data exploration
6. **Main Analysis** - Core analysis code
7. **Results and Visualization** - Visualizations and result presentation
8. **Findings and Conclusions** - Summary of key findings, conclusions, and next steps

## Best Practices

### Auto-Reloading Modules

The template includes the `setup_notebook()` utility that enables auto-reloading of modules:

```python
from {{ package_name }}.utils.notebook import setup_notebook
setup_notebook()
```

This allows you to:
1. Edit a module in your project package
2. Save the file
3. Run notebook cells again - they will use the updated module code

This provides a smooth workflow when developing modules and using them in notebooks.

### Environment Management

For notebook dependencies:

1. **Use Project Dependencies** - All standard notebook dependencies are included in the project's optional dependencies
2. **Installation** - Install with `pip install -e '.[notebooks]'`
3. **Special Dependencies** - If a notebook requires additional dependencies beyond those in the project:
   - Document them clearly in a markdown cell at the top of the notebook
   - Consider adding them to the project's `pyproject.toml` if they become common requirements

### Security Considerations

When working with notebooks:

1. **Clear Outputs Before Committing** - Always clear notebook outputs before committing to version control
2. **Avoid Sensitive Data** - Never store API keys, credentials, or sensitive data in notebooks
3. **Use Environment Variables** - Load sensitive configuration from environment variables, not hardcoded

### Code Migration

As you develop code in notebooks:

1. Start with exploratory code directly in notebook cells
2. Refactor reusable functions to appropriate modules in `src/`
3. Update notebooks to import functionality from modules
4. Add tests for the extracted code
5. Use notebooks to demonstrate and document the API
