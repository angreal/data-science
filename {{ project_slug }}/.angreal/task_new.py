import angreal
import os
import re
import json
from datetime import datetime
from pathlib import Path
import shutil

new = angreal.command_group(name='new', about='Create new project components')

@new()
@angreal.command(name='epoch', about='Start a new epoch of exploration')
@angreal.argument(name='description', long='description', short='d',
                 help='Short description of the epoch', required=False)
def new_epoch(description=""):
    """Create a new epoch directory with incrementing number."""

    # Get the notebooks directory
    # angreal.get_root() returns the .angreal directory, so we go up one level for project root
    angreal_dir = angreal.get_root()
    project_root = os.path.join(angreal_dir, "..")
    notebooks_dir = os.path.join(project_root, "notebooks")
    
    # Create notebooks directory if it doesn't exist
    os.makedirs(notebooks_dir, exist_ok=True)
    
    # Find the highest epoch number
    epoch_pattern = re.compile(r"epoch_(\d+)")
    highest_epoch = 0
    
    if os.path.exists(notebooks_dir):
        for item in os.listdir(notebooks_dir):
            if os.path.isdir(os.path.join(notebooks_dir, item)):
                match = epoch_pattern.match(os.path.basename(item))
                if match:
                    epoch_num = int(match.group(1))
                    highest_epoch = max(highest_epoch, epoch_num)
    
    # Create the new epoch directory
    new_epoch_num = highest_epoch + 1
    new_epoch_dir = os.path.join(notebooks_dir, f"epoch_{new_epoch_num:03d}")
    os.makedirs(new_epoch_dir, exist_ok=True)
    
    # Create README.md for the new epoch
    templates_dir = os.path.join(angreal_dir, "templates")
    readme_template = os.path.join(templates_dir, "notebooks", "epoch_readme.md")
    
    # Create context for template rendering
    context = {
        "epoch_number": f"{new_epoch_num:03d}",
        "epoch_description": description or f"Epoch {new_epoch_num:03d} exploration"
    }
    
    # Check if template exists
    if not os.path.exists(readme_template):
        print(f"Error: Template not found at {readme_template}")
        return
        
    # Render the template using Angreal's template system
    with open(readme_template, 'r') as f:
        template_content = f.read()
    
    # Render the template and write to file
    rendered_content = angreal.render_template(template_content, context)
    with open(os.path.join(new_epoch_dir, "README.md"), 'w') as f:
        f.write(rendered_content)
    
    print(f"Created new epoch directory: {new_epoch_dir}")
    print(f"Current working epoch is now: epoch_{new_epoch_num:03d}")


@new()
@angreal.command(name='notebook', about='Create a new notebook in the current epoch.')
@angreal.argument(name='title', long='title', short='t',
                 help='Title of the notebook', required=True)
@angreal.argument(name='author', long='author', short='a',
                 help='Author of the notebook', required=False)
@angreal.argument(name='epoch', long='epoch', short='e',
                 help='Specific epoch to create the notebook in (e.g., "001")', required=False)
def new_notebook(title, author=None, epoch=None):
    """Create a new notebook from template in the current or specified epoch."""

    # Get the notebooks directory
    # angreal.get_root() returns the .angreal directory, so we go up one level for project root
    angreal_dir = angreal.get_root()
    project_root = os.path.join(angreal_dir, "..")
    notebooks_dir = os.path.join(project_root, "notebooks")
    
    if not os.path.exists(notebooks_dir):
        print(f"Error: Notebooks directory not found at {notebooks_dir}")
        return
    
    # Find the current epoch if not specified
    if epoch is None:
        epoch_pattern = re.compile(r"epoch_(\d+)")
        highest_epoch = 0
        
        for item in os.listdir(notebooks_dir):
            if os.path.isdir(os.path.join(notebooks_dir, item)):
                match = epoch_pattern.match(item)
                if match:
                    epoch_num = int(match.group(1))
                    highest_epoch = max(highest_epoch, epoch_num)
        
        epoch = f"{highest_epoch:03d}"
    
    # Ensure epoch directory exists
    epoch_dir = os.path.join(notebooks_dir, f"epoch_{epoch}")
    if not os.path.exists(epoch_dir):
        print(f"Error: Epoch directory not found at {epoch_dir}")
        print(f"Use 'angreal new epoch' to create a new epoch first")
        return
    
    # Generate notebook filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    author_initials = "nn"  # Default to "nn" (no name) if author not provided
    
    if author:
        name_parts = author.split()
        if len(name_parts) >= 2:
            author_initials = (name_parts[0][0] + name_parts[-1][0]).lower()
        else:
            author_initials = name_parts[0][:2].lower()
    
    # Create a slug from the title
    title_slug = title.lower().replace(' ', '_')
    title_slug = re.sub(r'[^a-z0-9_]', '', title_slug)
    
    notebook_filename = f"{date_str}_{author_initials}_{title_slug}.ipynb"
    notebook_path = os.path.join(epoch_dir, notebook_filename)
    
    # Get the notebook template
    templates_dir = os.path.join(angreal_dir, "templates")
    notebook_template_path = os.path.join(templates_dir, "notebooks", "notebook_template.ipynb")
    
    try:
        # Get project info from context
        project_context = angreal.get_context()
        package_name = project_context.get('package_name', 'myproject')
        
        # Create context for template rendering
        context = {
            "notebook_title": title,
            "notebook_author": author or 'Anonymous',
            "notebook_date": date_str,
            "epoch_number": epoch,
            "package_name": package_name
        }
        
        # Check if template exists
        if not os.path.exists(notebook_template_path):
            print(f"Error: Template not found at {notebook_template_path}")
            return
        
        # Render the template using Angreal's template system
        with open(notebook_template_path, 'r') as f:
            template_content = f.read()
        
        # Render the template and write to file
        rendered_content = angreal.render_template(template_content, context)
        with open(notebook_path, 'w') as f:
            f.write(rendered_content)
        
        print(f"Created new notebook: {notebook_path}")
        
    except Exception as e:
        print(f"Error creating notebook: {e}")
        print(f"Exception details: {str(e)}")