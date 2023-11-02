"""
    ./topological_abelianization/hyperbolic_chern_insulator.py

    Author: Fabian R. Lux
    Date:   6/27/2023
    Mail:   fabian.lux@yu.edu

    We implement the model proposed in 

    https://doi.org/10.1038/s41467-023-36767-8

    for a hyperbolic Chern insulator with non-trivial second Chern number. We investigate,
    whether the band gaps of the system remain open in the thermodynamic limit.
"""

import json
import sys
import numpy as np
import matplotlib.pyplot as plt

import scipy

import kpm
from input import *
from fuchsian import *

from clifford_algebra import gamma
from mpicontrol import MPIControl

# -- parameters 

m = 0.7
a = 0.2

n_energies = 500
n_moments = 10
n_random_states = 20

# --  initialize basis objects

with open('./lexikon.json', 'r') as file:
    json_data = json.load(file)

basis = [Fuchsian(word=f['word'], n=f['n'])%N for f in json_data]
d = len(basis)

hashed_basis = [b.hash for b in basis]

dict_basis = {}

for i in range(len(basis)):
    dict_basis[str(hashed_basis[i])] = i


def represent(op):
    """
        op: integer index of the operator in the basis
    """

    representation = scipy.sparse.lil_matrix((d, d), dtype=complex)
    for j in range(d):
        c = (op*basis[j]) % N

        i = dict_basis[str(c.hash)]

        representation[i, j] += 1

    return representation

# H_operators = [ Fuchsian(word=[w]) for w in generators ]


H = scipy.sparse.lil_matrix((4*d, 4*d), dtype=complex)

S_dict = {}

# print("Representing the operators :)")

S_dict['0'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['a₁']) % N), dtype=complex)
S_dict['1'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['a₂']) % N), dtype=complex)
S_dict['2'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['b₁']) % N), dtype=complex)
S_dict['3'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['b₂']) % N), dtype=complex)

def S(i):
    return S_dict[str(i)]

for i in range(4):
    H += scipy.sparse.kron(scipy.sparse.lil_matrix(gamma[i]), S(i)- S(i).T ) / (2*1j) \
        +scipy.sparse.kron(scipy.sparse.lil_matrix(gamma[4]),  S(i)+ S(i).T ) / 2

H += m * scipy.sparse.lil_matrix( np.kron( gamma[4], np.eye(d,dtype=complex)) )

energy, dos = kpm.density_of_states(H, scale=100, n_moments=n_moments, n_energies=n_energies, n_random_states=n_random_states)

np.save("./out/hyperbolic_chern_energy.npy", energy)
np.save("./out/hyperbolic_chern_dos.npy", dos)       
