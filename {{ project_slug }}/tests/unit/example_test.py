# tests/unit/example_test.py
"""Example test file demonstrating the recommended testing pattern.

This file serves as a template for how tests should be structured.
Developers should create test files mirroring the module structure
of the src directory.
"""

import pytest

def test_example():
    """Simple example test to demonstrate the test structure."""
    # Arrange
    expected = 4
    
    # Act
    result = 2 + 2
    
    # Assert
    assert result == expected

class TestExampleClass:
    """Example test class to demonstrate class-based test organization."""
    
    def setup_method(self):
        """Setup method run before each test."""
        self.value = 10
    
    def test_value(self):
        """Test that the value is set correctly."""
        assert self.value == 10
    
    def test_multiplication(self):
        """Test that multiplication works correctly."""
        assert self.value * 2 == 20
