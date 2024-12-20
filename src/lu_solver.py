"""
Module with the LUSolver class
"""

import numpy as np

# from scipy.linalg import lu_factor, lu_solve


class LUSolver:
    """
    LU solver
    """

    def __init__(self, input_matrix: np.ndarray):
        """
        Constructor of the class. It takes the input matrix and decompose it into LU factorization.
        Store the factorization and permutation into class members.
        """
        pass

    def solve(self, b: np.ndarray) -> np.ndarray:
        """
        Solve the linear equation with the input matrix and the given vector b.
        """
        pass
