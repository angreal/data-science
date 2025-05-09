# {{ project_name }}

{{ project_desc_short }}

## Documentation

This documentation follows the [Diátaxis framework](https://diataxis.fr/), organized into four main sections:

- **[Tutorials](tutorials/getting-started.md)**: Step-by-step guides to get you started
- **[How-To Guides](how-to/index.md)**: Practical guides for specific tasks
- **[Reference](reference/index.md)**: Technical information and API documentation
- **[Explanation](explanation/index.md)**: Background, context, and design decisions

## Installation

```bash
# Install the package
pip install {{ package_name }}

# For development (including documentation tools)
pip install -e ".[docs]"
```

## Building Documentation

To build and view this documentation locally:

```bash
# Install documentation dependencies if not already installed
pip install -e ".[docs]"

# Serve the documentation
angreal docs serve
```

Then open http://127.0.0.1:8000 in your browser.
