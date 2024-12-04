import numpy as np
import pytest

from ees_scientific_software_engineering.rms import rms


def test_rms():
    input_array = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    isinstance(rms(input_array), float)
