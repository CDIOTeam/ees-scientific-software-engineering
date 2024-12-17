"""
    This module to calculate the RMS of an array
"""

import numpy as np
import pytest

from ees_scientific_software_engineering.rms import rms


def test_rms():
    """
    Testing root mean square
    """
    input_array = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    result = np.sqrt((1.0**2 + 2.0**2 + 3.0**2 + 4.0**2) / 5)
    isinstance(rms(input_array), float)
    assert np.isclose(rms(input_array), result)


def test_rms_invalid_dimension():
    """
    Testing dimension of numpy array
    """
    input_array = np.array([[1.0, 2.0], [3.0, 4.0]])  # 2D array
    with pytest.raises(ValueError, match="input_array must be one-dimensional"):
        rms(input_array)


def test_input_type_rms():
    input_array = [0.0, 1.0, 2.0, 3.0, 4.0]
    with pytest.raises(TypeError, match="input_array should be a numpy array"):
        rms(input_array)


def test_rms_with_nan():
    """Test RMS raises ValueError if input contains NaN."""
    input_array = np.array([1.0, np.nan, 2.0], dtype=np.float64)
    with pytest.raises(ValueError, match="input_array must not contain any NaN values"):
        rms(input_array)


def test_rms_with_inf():
    """Test RMS raises ValueError if input contains Inf."""
    input_array = np.array([1.0, np.inf, 2.0], dtype=np.float64)
    with pytest.raises(ValueError, match="input_array must not contain any Inf values"):
        rms(input_array)
