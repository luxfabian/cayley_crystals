import json
import sys
import numpy as np
import matplotlib.pyplot as plt

import scipy

from input import *
from fuchsian import *

from clifford_algebra import gamma
from mpicontrol import MPIControl

# --  initialize basis objects

with open('./lexikon.json', 'r') as file:
    json_data = json.load(file)

basis = [Fuchsian(word=f['word'], n=f['n'])%N for f in json_data]
d = len(basis)

hashed_basis = [b.hash for b in basis]

dict_basis = {}

for i in range(len(basis)):
    dict_basis[str(hashed_basis[i])] = i

# if len(hashed_basis) == len(np.unique(hashed_basis)):
#     print("Basis hashing succesful!")
# else:
#     print("ERROR: Basis hashing failed")
#     raise


def represent(op):
    """
        op: integer index of the operator in the basis
    """

    representation = scipy.sparse.lil_matrix((d, d), dtype=complex)
    for j in range(d):
        c = (op*basis[j]) % N

        i = dict_basis[str(c.hash)]

        representation[i, j] = 1

    return representation

H_operators = [ Fuchsian(word=[w]) for w in generators ]


def topo_spectrum(m):

    H = scipy.sparse.lil_matrix((4*d, 4*d), dtype=complex)

    S_dict = {}

    # print("Representing the operators :)")

    S_dict['0'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['a₁']) % N), dtype=complex)
    S_dict['1'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['a₂']) % N), dtype=complex)
    S_dict['2'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['b₁']) % N), dtype=complex)
    S_dict['3'] = scipy.sparse.lil_matrix( represent(Fuchsian(word=['b₂']) % N), dtype=complex)
    
    def S(i):
        return S_dict[str(i)]

    # print(scipy.sparse.kron( scipy.sparse.lil_matrix(gamma[1]), S(0)- S(0).T ))

    # print("And setting up the Hamiltonian now!")

    for i in range(4):
       H += scipy.sparse.kron( scipy.sparse.lil_matrix(gamma[i+1]), S(i)- S(i).T ) / (2*1j) +scipy.sparse.kron(scipy.sparse.lil_matrix(gamma[0]),  S(i)+ S(i).T ) / 2

    H += m * scipy.sparse.lil_matrix( np.kron( gamma[0], np.eye(d,dtype=complex)) )

    import kpm
    import matplotlib.pyplot as plt


    scale = 20 # this number has to be such that max(|eigenvalues|)/scale < 1
    npol = 400 # number of polynomials, energy resolution goes as 1/npol
    ne = 400 # number of energies to calculate (between -scale and scale)
    ntries = 10 # number of random vectors used
    # returns energies and dos

    (x1,y1) = kpm.density_of_states(H,n_random_states=ntries,scale=scale,n_moments=npol,n_energies=ne)
    
    
   

    # plt.plot(x1,y1) # plot this dos
    # plt.show()

    return y1


def run():
    
    MPI = MPIControl()

    nm = 200
    ms = np.linspace(-8,8, nm)

    if MPI.is_root():
        np.save('./spectra/ms.npy', ms)

    for i in range(nm):
        if MPI.my_turn(i):
            m = ms[i]
            spec = topo_spectrum(m)

            fname = './spectra/'+str(i).zfill(5)+'.npy'
            np.save(fname, spec)

    MPI.print("All is done!")
    MPI.finalize()

if __name__ == "__main__":
    run()


    