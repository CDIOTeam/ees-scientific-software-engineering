"""
    This module to calculate the RMS of an array
"""
import numpy as np
import pytest

from ees_scientific_software_engineering.rms import rms


def test_rms():
<<<<<<< HEAD
    """
        Testing root mean square
    """
=======
    """Check the output for the rms function for a simple case"""
>>>>>>> main
    input_array = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    result = np.sqrt((1.0**2 + 2.0**2 + 3.0**2 + 4.0**2) / 5)
    isinstance(rms(input_array), float)
    assert np.isclose(rms(input_array), result)

<<<<<<< HEAD
def test_rms_invalid_dimension():
    """
        Testing dimension of numpy array
    """
    input_array = np.array([[1.0, 2.0], [3.0, 4.0]])  # 2D array
    with pytest.raises(ValueError, match="input_array must be one-dimensional"):
=======

def test_input_type_rms():
    input_array = [0.0, 1.0, 2.0, 3.0, 4.0]
    with pytest.raises(TypeError, match="input_array should be a numpy array"):
>>>>>>> main
        rms(input_array)
