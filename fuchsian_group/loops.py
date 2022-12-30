import json
import scipy
import numpy as np
import matplotlib.pyplot as plt

import input
from fuchsian import *

# -- load Hamiltonian
H = scipy.sparse.load_npz('./hamiltonian.npz')

d = H.shape[0]

def loops(n):
    """
        Calculates N_e(n) = <e| H^n |e> by applying H repeatetly to |e>
    """

    # -- vector corresponding to identity element
    v = np.zeros(d, dtype=complex)
    v[0] = 1

    for i in range(n):
        print(i, v[0])
        v = H.dot(v)


if __name__ == "__main__":
    loops(100)


    