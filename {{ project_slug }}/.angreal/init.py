import angreal
import os
import shutil
import time


def init():
    """Initialize the data science project with selected components."""
    
    # Get the project root using angreal utility function
    project_root = angreal.get_root()
    
    # Get the context
    context = angreal.get_context()
    
    # Extract common variables - no default values to ensure errors are raised if missing
    package_name = context.get('package_name')
    
    # Get boolean values from context
    with_database = context.get('with_database') == 'true'
    with_frontend = context.get('with_frontend') == 'true'
    with_app = context.get('with_app') == 'true'
    
    # Templates directory is under .angreal directory
    templates_dir = os.path.join(project_root, "templates")
    
    print(f"\nInitializing project with options:")
    print(f"- Database: {with_database}")
    print(f"- Frontend: {with_frontend}")
    print(f"- App: {with_app}")
    print("\nDatabase and frontend components are included in base installation.")
    print(f"Install the package with: pip install -e '.'")
    print(f"For development tools: pip install -e '.[dev]'")
    print(f"For full installation with all tools: pip install -e '.[all]'")
    
    # Set up database if requested
    if with_database:
        setup_database(project_root, templates_dir, package_name, context)
    
    # Set up frontend if requested
    if with_frontend:
        setup_frontend(project_root, templates_dir, context)
    
    # Set up app deployment if requested
    if with_app:
        setup_app(project_root, templates_dir, context)
    
    print("Project initialization complete!")


def setup_database(project_root, templates_dir, package_name, context):
    """Set up SQLAlchemy database with migrations."""
    
    # Create database directory structure
    db_dir = os.path.join(project_root, "src", package_name)
    models_dir = os.path.join(db_dir, "models")
    migrations_dir = os.path.join(models_dir, "migrations")
    versions_dir = os.path.join(migrations_dir, "versions")
    
    # Create directories
    os.makedirs(db_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(migrations_dir, exist_ok=True)
    os.makedirs(versions_dir, exist_ok=True)
    
    # Copy and render database templates
    template_files = [
        # Models directory files
        ("database/models/__init__.py", os.path.join(models_dir, "__init__.py")),
        ("database/models/base.py", os.path.join(models_dir, "base.py")),
        
        # Migrations files
        ("database/migrations/__init__.py", os.path.join(migrations_dir, "__init__.py")),
        ("database/migrations/env.py", os.path.join(migrations_dir, "env.py")),
        ("database/migrations/versions/__init__.py", os.path.join(versions_dir, "__init__.py")),
        ("database/alembic.ini", os.path.join(project_root, "alembic.ini")),
    ]
    
    for src_path, dest_path in template_files:
        # Use angreal's template renderer
        template_path = os.path.join(templates_dir, src_path)
        
        # Check if template exists
        if not os.path.exists(template_path):
            print(f"Warning: Template not found at {template_path}, skipping...")
            continue
            
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Render the template and write to file
        rendered_content = angreal.render_template(template_content, context)
        with open(dest_path, 'w') as f:
            f.write(rendered_content)
    
    # Update settings.py to include database configuration
    settings_path = os.path.join(project_root, "src", package_name, "core", "settings.py")
    
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            content = f.read()
        
        # Add database settings if not already present
        if "DATABASE_URL" not in content:
            db_settings = """
# Database settings
DATABASE_URL: str = "sqlite:///./app.db"
"""
            with open(settings_path, "a") as f:
                f.write(db_settings)
    
    # Inform the user about the database setup and available commands
    print("\nDatabase support added!")
    print("To create a new model, run: angreal new-model ModelName")


def setup_frontend(project_root, templates_dir, context):
    """Set up Streamlit frontend."""
    
    # Create frontend directory
    frontend_dir = os.path.join(project_root, "frontend")
    os.makedirs(frontend_dir, exist_ok=True)
    
    # Inform the user about the frontend setup
    print("\nFrontend support added!")


def setup_app(project_root, templates_dir, context):
    """Set up application deployment scripts."""
    
    # Create deployment directory
    deploy_dir = os.path.join(project_root, "deployment")
    os.makedirs(deploy_dir, exist_ok=True)
    
    # Copy and render deployment templates
    template_files = [
        ("deployment/app.sh", os.path.join(deploy_dir, "app.sh")),
    ]
    
    for src_path, dest_path in template_files:
        # Use angreal's template renderer
        template_path = os.path.join(templates_dir, src_path)
        
        # Check if template exists
        if not os.path.exists(template_path):
            print(f"Warning: Template not found at {template_path}, skipping...")
            continue
            
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Render the template and write to file
        rendered_content = angreal.render_template(template_content, context)
        with open(dest_path, 'w') as f:
            f.write(rendered_content)
    
    # Make app.sh executable
    os.chmod(os.path.join(deploy_dir, "app.sh"), 0o755)
    
    # Inform the user how to install app deployment dependencies
    print("\nApp deployment support added! You can install it with:")
    print(f"pip install -e '.[app]'")
