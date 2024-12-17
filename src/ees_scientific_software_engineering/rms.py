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
    """
    if not isinstance(input_array, np.ndarray):
        raise TypeError("input_array should be a numpy array")

    return np.sqrt(np.mean(input_array**2))
