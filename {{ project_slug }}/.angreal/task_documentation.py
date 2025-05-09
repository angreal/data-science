import angreal
import subprocess
import sys

docs = angreal.command_group(name='docs', about='Documentation management commands')

@docs()
@angreal.command(name='build', about='Build the documentation')
def build_docs():
    """Build the MkDocs documentation into static files."""
    try:
        # Install docs dependencies if needed
        install_docs_deps()
        
        # Build the docs
        subprocess.run(["mkdocs", "build"], check=True)
        
        print("Documentation built successfully. Output is in the 'site' directory.")
    except subprocess.CalledProcessError as e:
        print(f"Error building documentation: {e}", file=sys.stderr)
        sys.exit(1)

@docs()
@angreal.command(name='serve', about='Serve the documentation locally')
@angreal.argument(name='port', long='port', short='p', 
                 help='Port to serve documentation on', default_value='8000')
def serve_docs(port='8000'):
    """Serve the documentation locally for development."""
    try:
        # Install docs dependencies if needed
        install_docs_deps()
        
        # Serve the docs on specified port
        subprocess.run(["mkdocs", "serve", f"--dev-addr=127.0.0.1:{port}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error serving documentation: {e}", file=sys.stderr)
        sys.exit(1)

def install_docs_deps():
    """Install documentation dependencies if needed."""
    try:
        # Check if mkdocs is installed
        subprocess.run(["mkdocs", "--version"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing documentation dependencies...")
        
        # Try to install the docs dependencies from the package
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".[docs]"], 
                           check=True)
        except subprocess.CalledProcessError:
            # Fall back to direct installation of key packages
            subprocess.run([
                sys.executable, "-m", "pip", "install",
                "mkdocs", "mkdocs-material", "mkdocstrings", "mkdocstrings-python"
            ], check=True)
        
        print("Documentation dependencies installed successfully.")
