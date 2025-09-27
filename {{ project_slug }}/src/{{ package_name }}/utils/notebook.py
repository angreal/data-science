"""Notebook utilities for Jupyter development."""

import logging
import sys
from pathlib import Path

# Configure logging
logger = logging.getLogger(__name__)


def setup_notebook(
    autoreload: bool = True,
    autoreload_mode: int = 2,
    add_project_root: bool = True,
) -> None:
    """Set up a Jupyter notebook with common configurations for the project.

    This function configures the notebook environment with common settings used across
    the project's notebooks. It handles:

    1. IPython autoreload configuration for development
    2. Project root path setup for imports

    Args:
        autoreload: Whether to enable IPython autoreload. When enabled, modules
            will be automatically reloaded when modified, making development easier.
            Defaults to True.

        autoreload_mode: Autoreload mode to use:
            - 0: Disabled
            - 1: Only reloads modules explicitly imported with %aimport
            - 2: Reloads all modules before executing code (except explicitly imported)
            Defaults to 2 (most aggressive mode).

        add_project_root: Whether to add the project root directory to the Python path.
            This ensures that imports from the package work correctly.
            Defaults to True.

    Examples:
        Basic usage with all defaults:
        >>> from {{ package_name }}.utils.notebook import setup_notebook
        >>> setup_notebook()

        Custom configuration:
        >>> setup_notebook(
        ...     autoreload=True,
        ...     autoreload_mode=1,  # Only reload explicit imports
        ...     add_project_root=True,
        ... )

    Notes:
        - The function includes error handling for missing dependencies
        - Warning messages are printed if features can't be enabled
        - This function should be called at the start of each notebook
        - The autoreload feature is particularly useful during development
    """
    # Enable auto-reloading if requested
    if autoreload:
        try:
            from IPython import get_ipython

            ipython = get_ipython()
            if ipython is not None:
                ipython.run_line_magic('load_ext', 'autoreload')
                ipython.run_line_magic('autoreload', str(autoreload_mode))
        except ImportError:
            logger.warning('IPython not available, autoreload not enabled')

    # Add project root to Python path if requested
    if add_project_root:
        # Get the project root by going up from the current module's location
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent.parent
        if str(project_root) not in sys.path:
            sys.path.append(str(project_root))