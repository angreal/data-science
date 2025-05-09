"""
Task to create a new database model file.
"""

import angreal
import os
import re

# Create a command group for new model commands
new = angreal.command_group(name='new', about='Create new project components')

@new()
@angreal.command(name='model', about='Create a new database model')
@angreal.argument(name='name', long='name', short='n',
                 help='Model name (CamelCase, e.g., "UserProfile")',
                 required=True)
@angreal.argument(name='description', long='description', short='d',
                 help='Optional description for the model',
                 required=False)
@angreal.argument(name='table', long='table', short='t',
                 help='Database table name (defaults to snake_case of model name)',
                 required=False)
def new_model(name, description=None, table=None):
    """Create a new database model file."""
    # Get project root and package name
    project_root = angreal.get_root()
    context = angreal.get_context()
    package_name = context.get('package_name')
    
    # Generate defaults if not provided
    if not description:
        description = f"{name} model representing {title_case(name)} data."
    
    if not table:
        table = snake_case(name) + 's'
    
    # Set up paths
    models_dir = os.path.join(project_root, "src", package_name, "models")
    model_file = os.path.join(models_dir, f"{snake_case(name)}.py")
    templates_dir = os.path.join(project_root, "templates")
    
    # Check if models directory exists
    if not os.path.exists(models_dir):
        print(f"Creating models directory: {models_dir}")
        os.makedirs(models_dir, exist_ok=True)
    
    # Check if model file already exists
    if os.path.exists(model_file):
        print(f"Error: Model file already exists: {model_file}")
        return
    
    # Prepare context for template
    template_context = {
        "model_name": name,
        "model_name_title": title_case(name),
        "model_description": description,
        "table_name": table
    }
    
    # Render template using Angreal
    template_path = os.path.join(templates_dir, "database", "models", "model.py")
    
    # Check if template exists
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        return
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Render the template and write to file
    rendered_content = angreal.render_template(template_content, template_context)
    with open(model_file, 'w') as f:
        f.write(rendered_content)
    
    # Update __init__.py
    update_init_file(models_dir, name)
    
    print(f"Created new model: {name}")
    print(f"Model file: {model_file}")
    print("Remember to run migrations to update your database schema.")


def update_init_file(models_dir, model_name):
    """Update __init__.py to import the new model."""
    init_path = os.path.join(models_dir, "__init__.py")
    
    with open(init_path, "r") as f:
        content = f.read()
    
    # Add import statement
    import_pattern = r"# Import models\n"
    import_statement = f"from .{snake_case(model_name)} import {model_name}\n"
    if "from ." + snake_case(model_name) in content:
        print(f"Model {model_name} already imported in __init__.py")
    else:
        content = re.sub(
            import_pattern, 
            f"# Import models\n{import_statement}", 
            content
        )
    
    # Add to __all__ list
    all_pattern = r"__all__ = \[\n    'Base',"
    all_statement = f"\n    '{model_name}',"
    if f"'{model_name}'" in content:
        print(f"Model {model_name} already in __all__ list")
    else:
        content = re.sub(
            all_pattern, 
            f"__all__ = [\n    'Base',{all_statement}", 
            content
        )
    
    with open(init_path, "w") as f:
        f.write(content)


def snake_case(text):
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def title_case(text):
    """Convert CamelCase or snake_case to Title Case."""
    # First handle snake_case
    words = text.replace('_', ' ').split()
    # Then handle CamelCase
    result = []
    for word in words:
        # Split CamelCase
        word_parts = re.findall(r'[A-Z]?[a-z]+', word)
        result.extend(word_parts)
    
    return ' '.join(word.capitalize() for word in result)
