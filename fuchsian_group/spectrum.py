"""
    ./fuchsian_group/spectrum.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Reads previousy determined  basis elements from ./lexikon.json
    Then, the Hamiltonian is set up and diagonalized.
    The spectrum is stored to ./spectrum.npy in binary (and ./spectrum.dat as CSV)
"""
import json
import numpy as np
import matplotlib.pyplot as plt

import input
from fuchsian import *

# --  initialize basis objects

with open('./lexikon.json', 'r') as file:
    json_data = json.load(file)

basis = [Fuchsian(word=f['word'], n=f['n']) %
         (input.p ** input.N) for f in json_data]
d = len(basis)

hashed_basis = [b.hash for b in basis]

dict_basis = {}

for i in range(len(basis)):
    dict_basis[str(hashed_basis[i])] = i

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
        c = (op*basis[j]) % (input.p ** input.N)

        i = dict_basis[str(c.hash)]

        representation[i, j] = 1

    return representation


H_operators = [Fuchsian(word=[w]) for w in generators]

H = np.zeros((d, d), dtype=int)

for g in H_operators:
    H = H + represent(g)

print("Calculating the spectrum...")
spectrum, _ = np.linalg.eigh(H)

np.savetxt('./spectrum.dat', spectrum)
np.save('./spectrum.npy', spectrum)

print("Spectrum strored in ./spectrum.npy and ./spectrum.dat")
