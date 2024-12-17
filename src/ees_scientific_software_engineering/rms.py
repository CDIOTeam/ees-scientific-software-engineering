"""
    This module to calculate the RMS of an array
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

    if input_array.ndim != 1:
        raise ValueError("input_array must be one-dimensional")

    return np.sqrt(np.mean(input_array**2))
