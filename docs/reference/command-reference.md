# Command Reference

This page documents all available commands provided by the template through the Angreal task system.

## Project Commands

### Initialize Project

```bash
angreal init https://github.com/yourusername/data-science-template.git
```

Initializes a new project from the template.

**Options**:
- None (follows interactive prompts)

**Example**:
```bash
# Initialize a new project
angreal init https://github.com/yourusername/data-science-template.git
```

## Epoch Commands

### Create a New Epoch

```bash
angreal new epoch [options]
```

Creates a new epoch directory in the notebooks folder with incrementing numbers.

**Options**:
- `--description`: Short description of the epoch

**Example**:
```bash
# Create a new epoch with a description
angreal new epoch --description "Feature engineering for customer segmentation"
```

## Notebook Commands

### Create a New Notebook

```bash
angreal new notebook [options]
```

Creates a new notebook from a template in the current or specified epoch.

**Options**:
- `--title`: Title of the notebook (required)
- `--author`: Author of the notebook
- `--epoch`: Specific epoch to create the notebook in (e.g., "001")

**Examples**:
```bash
# Create a notebook in the current epoch
angreal new notebook --title "Exploratory Data Analysis" --author "Your Name"

# Create a notebook in a specific epoch
angreal new notebook --title "Feature Selection" --author "Your Name" --epoch "002"
```

## Documentation Commands

### Build Documentation

```bash
angreal docs build
```

Builds the documentation site.

**Options**:
- None

**Example**:
```bash
# Build documentation
angreal docs build
```

### Serve Documentation

```bash
angreal docs serve [options]
```

Serves the documentation site locally for preview.

**Options**:
- `--port`: Port to serve the documentation on (default: 8000)

**Example**:
```bash
# Serve documentation on the default port
angreal docs serve

# Serve documentation on a specific port
angreal docs serve --port 8080
```

## Database Commands

### Create a New Model

```bash
angreal new-model [options]
```

Creates a new database model file.

**Options**:
- `model_name`: Model name in CamelCase (required)
- `description`: Optional description for the model
- `table_name`: Database table name (defaults to snake_case of model name)

**Example**:
```bash
# Create a new model
angreal new-model UserProfile --description "User profile information" --table_name "user_profiles"
```

### Run Migrations

```bash
angreal db migrate [options]
```

Creates a new migration or runs existing migrations.

**Options**:
- `--message`: Migration message (when creating a new migration)
- `--upgrade`: Upgrade the database to the latest version

**Examples**:
```bash
# Create a new migration
angreal db migrate --message "Add user profiles table"

# Upgrade the database to the latest version
angreal db migrate --upgrade
```

## Testing Commands

### Run Tests

```bash
angreal test [options]
```

Runs the test suite.

**Options**:
- `--unit`: Run unit tests only
- `--integration`: Run integration tests only
- `--functional`: Run functional tests only
- `--notebooks`: Run notebook tests
- `--epoch`: Specific epoch to test notebooks from (e.g., "001")
- `--coverage`: Generate coverage report

**Examples**:
```bash
# Run all tests
angreal test

# Run unit tests only
angreal test --unit

# Run notebook tests for a specific epoch
angreal test --notebooks --epoch 001

# Run tests with coverage report
angreal test --coverage
```

## Environment Commands

### Create Environment

```bash
angreal env create [options]
```

Creates a virtual environment for the project.

**Options**:
- `--name`: Name of the environment (default: project name)
- `--python`: Python version to use (default: current version)

**Example**:
```bash
# Create a virtual environment
angreal env create

# Create a virtual environment with specific Python version
angreal env create --python 3.9
```

### Install Dependencies

```bash
angreal env install [options]
```

Installs project dependencies.

**Options**:
- `--dev`: Install development dependencies
- `--docs`: Install documentation dependencies
- `--notebooks`: Install notebook dependencies
- `--all`: Install all dependencies

**Examples**:
```bash
# Install base dependencies
angreal env install

# Install all dependencies
angreal env install --all

# Install specific dependency groups
angreal env install --dev --notebooks
```

## Deployment Commands

### Build Docker Image

```bash
angreal deploy build [options]
```

Builds a Docker image for the project.

**Options**:
- `--tag`: Tag for the Docker image (default: project name)

**Example**:
```bash
# Build Docker image with default tag
angreal deploy build

# Build Docker image with specific tag
angreal deploy build --tag myproject:latest
```

### Run Docker Container

```bash
angreal deploy run [options]
```

Runs the project in a Docker container.

**Options**:
- `--port`: Port to expose (default: 8000)
- `--detach`: Run container in background

**Example**:
```bash
# Run Docker container
angreal deploy run

# Run Docker container on specific port in background
angreal deploy run --port 8080 --detach
```

## Combining Commands

Commands can be combined to perform multiple actions in sequence:

```bash
# Create a new epoch and a notebook in it
angreal new epoch --description "Feature Engineering" && \
angreal new notebook --title "Feature Selection" --author "Your Name"

# Run tests and build documentation
angreal test && angreal docs build
```

## Command Customization

The template's task system is built with Angreal, which allows for customization and extension. You can add new commands or modify existing ones by editing the task files in the `.angreal` directory.

For example, to add a new command for generating reports:

1. Create a new file `.angreal/task_report.py`
2. Define your command using the Angreal API
3. Implement the command functionality

See the [Angreal documentation](https://angreal.github.io/angreal/) for more details on creating custom commands.

## Environment Variables

Some commands may be affected by environment variables:

- `PYTHONPATH`: Affects Python module imports
- `ANGREAL_ENV`: Determines which environment configuration to use
- `<PROJECT_PREFIX>_*`: Project-specific environment variables

## Further Reading

For more detailed information about specific commands, see:

- [Getting Started Guide](../how-to/getting-started.md): Basic usage of the template commands
- [Adding Epochs](../how-to/adding-epochs.md): Working with epochs and notebooks
- [Creating Models](../how-to/creating-models.md): Database model commands
- [Testing](../how-to/testing.md): Running and writing tests
- [Deployment](../how-to/deployment.md): Deploying your project
