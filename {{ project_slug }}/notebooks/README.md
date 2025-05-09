# Notebooks Directory

This directory contains all Jupyter notebooks organized by development phase and purpose.

## Structure

```
notebooks/
├── epoch_001/        # First development/experimental phase
├── epoch_00N/        # Nth development/experimental phase
└── templates/        # For notebook templates and common utilities
```

## Guidelines

### Organization
- Notebooks are organized by their purpose (exploration, modeling, evaluation, production)
- Each directory must contain a README.md describing its purpose and contents
- Notebooks within directories should be chronologically ordered

### Epoch Organization
- Each epoch should have its own directory with a descriptive name (e.g., `epoch_001`)
- Each epoch directory must contain a README.md describing the epoch's purpose and outcomes
- Notebooks within epochs should be chronologically ordered

### Notebook Naming Convention
```
YYYY-MM-DD_author_initials_short_descriptive_name.ipynb
```
Example: `2024-03-04_ds_feature_exploration.ipynb`

### Notebook Structure
- Use the template from `templates/notebook_template.ipynb`
- Keep notebooks focused and well-documented
- Include clear section headers and explanations
- Document key decisions and their rationale
- Start each notebook with the standard imports and setup:

```python
# Standard imports
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Enable auto-reloading of modules
from {{ package_name }}.utils.notebook import setup_notebook
setup_notebook()

# Import from the project package
from {{ package_name }}.data import loading
from {{ package_name }}.features import engineering
from {{ package_name }}.models import training
```

### Version Control
- Remove outputs before committing
- Use clear commit messages
- Consider using markdown exports for better diff viewing

## Creating a New Epoch

1. Create a new directory: `epoch_XXX`
2. Copy the README template and update it
3. Create notebooks following the naming convention
4. Update the main README with the new epoch information

## Best Practices

1. **Documentation**
   - Keep READMEs up to date
   - Document key decisions and their rationale
   - Include context and dependencies

2. **Organization**
   - Keep related work together
   - Use clear, descriptive names
   - Maintain chronological order

3. **Quality**
   - Review notebooks before committing
   - Remove unnecessary outputs (for security reasons)
   - Keep code clean and well-commented
   - Consider using `nbstripout` to automatically strip outputs before commits

4. **Code Integration**
   - Start with exploratory code in notebooks
   - Extract reusable code to modules in the `src/` directory
   - Update notebooks to import from modules
   - Add tests for the extracted code
   - Use notebooks to demonstrate and document the API

5. **Testing Notebooks**
   - Notebooks can be tested to ensure they execute without errors:

   ```bash
   # Test all notebooks
   angreal test --notebooks

   # Test a specific epoch
   angreal test --notebooks --epoch 001
   ```

   Note: These tests only check execution, not outputs, for security reasons.

6. **Notebook Environment**
   - All notebook dependencies are included in the project's optional dependencies
   - To install everything needed for notebooks:

   ```bash
   # Install the project with notebook dependencies
   pip install -e '.[notebooks]'
   ```

   - If a notebook requires additional dependencies, document them in the notebook's markdown cell
   - For epoch-specific environment notes, include them in the epoch's README.md 