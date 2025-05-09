# Adding and Managing Epochs

This guide explains how to use the epoch-based notebook organization system in the template, including creating new epochs, managing notebooks within epochs, and best practices.

## What Are Epochs?

In this template, "epochs" represent distinct phases of experimentation or development in your data science project. Each epoch is a separate directory containing notebooks and supporting files related to that phase.

Using epochs helps you:

1. Track the evolution of your project over time
2. Organize experiments into logical groups
3. Document your progress and decision-making
4. Maintain a clear history of your work

## Creating a New Epoch

The template provides a convenient command for creating new epochs:

```bash
angreal new epoch --description "Brief description of this phase"
```

This command:

1. Creates a new epoch directory in the `notebooks/` folder
2. Increments the epoch number automatically (e.g., `epoch_001` → `epoch_002`)
3. Creates a README.md file with your description
4. Sets up the directory structure for notebooks

### Example Epoch Descriptions

Here are some example descriptions for different types of epochs:

- "Initial data exploration and cleaning"
- "Feature engineering and selection"
- "Baseline model development"
- "Model optimization and hyperparameter tuning"
- "Validation and testing"
- "Final model packaging for production"

## Creating Notebooks in an Epoch

Once you've created an epoch, you can add notebooks to it:

```bash
angreal new notebook --title "Your Notebook Title" --author "Your Name"
```

By default, this creates a notebook in the latest epoch. To create a notebook in a specific epoch:

```bash
angreal new notebook --title "Your Notebook Title" --author "Your Name" --epoch "001"
```

### Notebook Naming Convention

The template automatically names notebooks following this convention:

```
YYYY-MM-DD_author_initials_short_descriptive_name.ipynb
```

For example:

```
2024-05-01_ds_data_exploration.ipynb
```

This naming convention helps maintain chronological order and clear authorship.

## Managing Epochs

### Updating Epoch README

Each epoch directory contains a README.md file that should describe:

1. The purpose of the epoch
2. Key experiments or analyses conducted
3. Main findings and decisions
4. Dependencies or prerequisites
5. Next steps or follow-up work

Keep this README updated as you add notebooks and make progress within the epoch.

### When to Create a New Epoch

Create a new epoch when:

1. **Starting a new phase**: Moving from exploration to modeling, or from baseline models to advanced models
2. **Changing direction**: Deciding to take a significantly different approach
3. **Revisiting earlier work**: Coming back to the project after some time
4. **Addressing new requirements**: Working on a new set of requirements or objectives

### Epoch Chronology

Epochs are numbered sequentially (001, 002, etc.) to maintain chronological order. This numbering helps track the evolution of your project over time.

## Best Practices

### Documentation

1. **Update READMEs regularly**: Keep epoch and notebook documentation up to date
2. **Document key decisions**: Record important decisions and their rationale
3. **Note dependencies**: Document any special dependencies or requirements

### Organization

1. **Keep related work together**: Group related notebooks within the same epoch
2. **Use clear, descriptive names**: Make notebook titles descriptive and specific
3. **Maintain chronological order**: Use dates in filenames to track progress

### Code Quality

1. **Refactor common code**: Move reusable code to the source package
2. **Update notebooks to use package code**: Import functions from your package
3. **Clean up before committing**: Remove unnecessary outputs and clean up code

### Version Control

1. **Commit regularly**: Make small, focused commits
2. **Use meaningful commit messages**: Describe what changed and why
3. **Consider using `nbstripout`**: Automatically strip notebook outputs before commits

## Example Epoch Structure

Here's an example structure for a mature project with multiple epochs:

```
notebooks/
├── README.md
├── epoch_001_initial_exploration/
│   ├── README.md
│   ├── 2024-05-01_ds_data_loading.ipynb
│   ├── 2024-05-02_ds_data_cleaning.ipynb
│   └── 2024-05-03_ds_exploratory_analysis.ipynb
├── epoch_002_feature_engineering/
│   ├── README.md
│   ├── 2024-05-10_ds_feature_selection.ipynb
│   ├── 2024-05-11_ds_feature_importance.ipynb
│   └── 2024-05-12_ds_feature_transformation.ipynb
├── epoch_003_baseline_models/
│   ├── README.md
│   ├── 2024-05-20_ds_linear_model.ipynb
│   ├── 2024-05-21_ds_tree_model.ipynb
│   └── 2024-05-22_ds_baseline_comparison.ipynb
└── epoch_004_advanced_models/
    ├── README.md
    ├── 2024-06-01_ds_neural_network.ipynb
    ├── 2024-06-02_ds_ensemble_methods.ipynb
    └── 2024-06-03_ds_model_comparison.ipynb
```

## Testing Notebooks

The template includes support for testing notebooks to ensure they execute without errors:

```bash
# Test all notebooks
angreal test --notebooks

# Test a specific epoch
angreal test --notebooks --epoch 001
```

These tests check that the notebooks execute successfully, helping catch issues early.

## Moving from Notebooks to Package Code

As your work in notebooks matures, consider moving reusable code to your source package:

1. Identify reusable components in your notebooks
2. Refactor them into functions or classes in your package
3. Update notebooks to import and use these functions
4. Add tests for the refactored code
5. Document the API in your package documentation

This approach improves code reusability, maintainability, and testability while keeping your notebooks focused on analysis and exploration.
