# How-To Guides

This section provides task-oriented guides for common operations when using the Data Science Template.

## Contents

- [Getting Started](getting-started.md): A guide to creating and setting up your first project
- [Adding Epochs](adding-epochs.md): How to use the epoch-based notebook organization system
- [Creating Models](creating-models.md): Creating database models with SQLAlchemy (coming soon)
- [Documentation](documentation.md): Writing and maintaining project documentation (coming soon)
- [Testing](testing.md): Writing and running tests for your project (coming soon)
- [Deployment](deployment.md): Deploying your project to production (coming soon)

## What are How-To Guides?

How-to guides are task-oriented documents that guide you through the steps required to solve a specific problem. Unlike tutorials, they assume you have basic familiarity with the template and focus on accomplishing specific tasks rather than teaching concepts.

### When to Use This Section

- When you need to accomplish a specific task
- When you know what you need to do but not how to do it
- When you need a reference for a procedure you've done before
- When you're troubleshooting a specific issue

## General Workflow

The general workflow for a data science project using this template follows these steps:

1. **Initialize the project**: Set up the project structure and dependencies
2. **Create epochs for exploration**: Organize your work into distinct phases
3. **Develop notebooks**: Explore data, build models, and document findings
4. **Refactor code**: Extract reusable code into the source package
5. **Write tests**: Ensure your code works as expected
6. **Document your work**: Keep documentation up to date
7. **Deploy your project**: Package and deploy your project

The how-to guides in this section cover each of these steps in detail, providing practical advice and examples.

## Common Tasks

Here are some quick references for common tasks:

### Creating a New Epoch

```bash
angreal new epoch --description "Brief description of this phase"
```

### Creating a New Notebook

```bash
angreal new notebook --title "Your Notebook Title" --author "Your Name"
```

### Installing Dependencies

```bash
# Install base package
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
angreal test

# Run unit tests only
angreal test --unit
```

### Building Documentation

```bash
# Build documentation
angreal docs build

# Serve documentation locally
angreal docs serve
```

For more detailed instructions, refer to the specific how-to guides in this section.
