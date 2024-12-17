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
    return np.sqrt(np.mean(input_array**2))
