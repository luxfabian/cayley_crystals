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

    scale = 8 # this number has to be such that max(|eigenvalues|)/scale < 1
    npol = 300 # number of polynomials, energy resolution goes as 1/npol
    ne = 300 # number of energies to calculate (between -scale and scale)
    ntries = 5 # number of random vectors used
    # returns energies and dos

    # (x1,y1) = kpm.tdos(H,ntries=ntries,scale=scale,npol=npol,ne=ne) 

    (x1,y1) = kpm.density_of_states(H, scale=scale, n_moments=npol, n_energies=ne, kernel="jackson",
         n_random_states=ntries, epsilon = 0.01)

    y1 = np.cumsum(y1)
    y1 = y1 / y1[-1]

    np.save('./energy.npy', x1)
    np.save('./ids.npy', y1)

    plt.plot(x1,y1) # plot this dos
    plt.title(r'Kernel polynomial method for $p=2$, $N=6$ and $p^N=64$')
    ax = plt.gca()
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$F(x)$')
    plt.grid()
    plt.savefig('./spec.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    kpm_solver()


    