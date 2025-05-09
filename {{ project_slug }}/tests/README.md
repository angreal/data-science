# Testing Guidelines

This directory contains the test suite for the project. Tests are organized to mirror the structure of the source code.

## Test Organization

- **Unit Tests (`tests/unit/`)**: Test individual components in isolation
- **Integration Tests (`tests/integration/`)**: Test how components work together
- **Functional Tests (`tests/functional/`)**: End-to-end tests for complete workflows

## Writing Tests

### Basic Test Structure

```python
# tests/unit/example_module/test_example.py

import pytest
from src.package_name.example_module import example_function

def test_example_function():
    # Arrange - Set up test data and expected outcomes
    input_data = [1, 2, 3]
    expected_result = 6
    
    # Act - Call the function being tested
    actual_result = example_function(input_data)
    
    # Assert - Verify the results are as expected
    assert actual_result == expected_result
```

### Class-Based Test Structure

```python
# tests/unit/example_module/test_example_class.py

import pytest
from src.package_name.example_module import ExampleClass

class TestExampleClass:
    def setup_method(self):
        # Setup code that runs before each test
        self.example = ExampleClass()
    
    def test_method_one(self):
        result = self.example.method_one()
        assert result == "expected_value"
    
    def test_method_two(self):
        result = self.example.method_two(input_value=10)
        assert result == 20
```

## Using Fixtures

Fixtures are defined in `conftest.py` files and provide reusable test components:

```python
# conftest.py
import pytest
import pandas as pd

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'id': range(1, 11),
        'value': [i * 2 for i in range(1, 11)]
    })

# Using the fixture in a test
def test_with_fixture(sample_dataframe):
    # The fixture is injected automatically
    assert len(sample_dataframe) == 10
```

## Running Tests

Use the provided Angreal task:

```bash
# Run all unit tests (default)
angreal test

# Run specific test types
angreal test --unit
angreal test --integration
angreal test --functional

# Run all tests
angreal test --all
```

## Test Files Naming Conventions

- Test filenames should start with `test_` and match the module they're testing
- Test functions should start with `test_`
- Test classes should start with `Test`

## Creating Unit Tests for a New Module

When creating a new module in the source code, also create a corresponding test file:

1. Create a new Python file in the appropriate subdirectory of `tests/unit/`
2. Name the file `test_<module_name>.py`
3. Import the module being tested
4. Write test functions/classes for the functionality

For example, if you create `src/data/preprocessing.py`, create `tests/unit/data/test_preprocessing.py`.

## Using Test-Driven Development (TDD)

For best results, follow the TDD approach:

1. Write a failing test for the functionality you want to add
2. Implement the functionality to make the test pass
3. Refactor the code while keeping the tests passing

This approach helps ensure your code is testable and meets requirements from the start.
