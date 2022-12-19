"""
    ./free_group/spectrum.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Reads previousy determined  basis elements from ./lexikon.npy
    Then, the Hamiltonian is set up and diagonalized.
    The spectrum is stored to ./spectrum.npy in binary (and ./spectrum.dat as CSV)
"""
import numpy as np
import matplotlib.pyplot as plt

import input
from group import *

# -- read basis elements from file
basis = np.array(np.load('./lexikon.npy'), dtype=int)
d = len(basis)

# -- generate hash for faster look-up
print("Hashing the basis...")
hashed_basis = [hash(str(b)) for b in basis]

dict_basis = {}

for i in range(len(basis)):
    dict_basis[hashed_basis[i]] = i

if len(hashed_basis) == len(np.unique(hashed_basis)):
    print("Basis hashing succesful!")
else:
    print("ERROR: Basis hashing failed")
    raise


def represent(op):
    """
        op: integer index of the operator in the basis
    """

    representation = np.zeros((d, d), dtype=int)
    for j in range(d):
        c = mult(op, basis[j], input.p ** input.N)

        c_hash = hash(str(c))

        i = dict_basis[c_hash]

        representation[i, j] = 1

    return representation


H_operators = [basis[1], basis[2], basis[3], basis[4]]

H = np.zeros((d, d), dtype=int)

for g in H_operators:
    H = H + represent(g)

print("Calculating the spectrum...")
spectrum, _ = np.linalg.eigh(H)

np.savetxt('./spectrum.dat', spectrum)
np.save('./spectrum.npy', spectrum)

print("Spectrum strored in ./spectrum.npy and ./spectrum.dat")
