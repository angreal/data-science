# tests/conftest.py

import os
import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope="session")
def sample_data():
    """Create a small sample DataFrame for testing."""
    return pd.DataFrame({
        'id': range(1, 101),
        'feature1': np.random.normal(0, 1, 100),
        'feature2': np.random.choice(['A', 'B', 'C'], 100),
        'target': np.random.choice([0, 1], 100)
    })

@pytest.fixture(scope="session")
def test_data_dir():
    """Return the path to the test data directory."""
    return os.path.join(os.path.dirname(__file__), 'data')
