import json
import sys
import numpy as np
import matplotlib.pyplot as plt
import kpm
import matplotlib.pyplot as plt

import scipy

import input
from fuchsian import *


# --  initialize basis objects

with open('./lexikon.json', 'r') as file:
    json_data = json.load(file)

basis = [Fuchsian(word=f['word'], n=f['n'])%(input.p**input.N) for f in json_data]
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
        c = (op*basis[j]) % (input.p**input.N)

        i = dict_basis[str(c.hash)]

        representation[i, j] = 1

    return representation


def kpm_solver():

    H = scipy.sparse.csr_matrix((d, d), dtype=complex)
    H_operators = [ Fuchsian(word=[w]) for w in generators ]

    for g in H_operators:
        H += represent(g)

    (E,dos) = kpm.density_of_states(H, scale=8, n_moments=300, n_energies=300, kernel="jackson",
         n_random_states=5, epsilon = 0.01)

    # -- numerical integration of DOS
    ids = np.cumsum(dos)
    ids = scipy.integrate.cumulative_trapezoid(dos, E, initial=0)

    # -- normalization
    ids = ids / ids[-1]

    np.save('./energy.npy', E)
    np.save('./ids.npy', ids)

    plt.plot(E,ids) # plot this dos
    plt.title(r'Kernel polynomial method for $p=2$, $N=6$ and $p^N=64$')
    ax = plt.gca()
    ax.set_xlabel(r'$\mu$')
    ax.set_ylabel(r'IDS($\mu$)')
    plt.grid()
    plt.savefig('./spec.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    kpm_solver()


    