""" 
This module contains the rms function
"""

import numpy as np


def rms(input_array: np.ndarray) -> float:
    """Calculate root mean square

    Args:
        input_array: np.array

    Returns:
        root mean square number

    Raises:
        ValueError: If input_array is not one-dimensional
    """
    if not isinstance(input_array, np.ndarray):
        raise TypeError("input_array should be a numpy array")

    if input_array.ndim != 1:
        raise ValueError("input_array must be one-dimensional")

    # Check for NaN values
    if np.isnan(input_array).any():
        raise ValueError("input_array must not contain any NaN values")

    # Check for Inf values
    if np.isinf(input_array).any():
        raise ValueError("input_array must not contain any Inf values")

    if not input_array.dtype == np.float64:
        raise TypeError("Array dtype is not np.float64")

    if not len(input_array) >= 1:
        raise ValueError("input_array must be of length >= 1")

    return np.sqrt(np.mean(input_array**2))
