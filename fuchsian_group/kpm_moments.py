"""
    ./fuchsian_group/kpm_moments.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Loads the KPM DOS from file and calculates the first moments of the
    DOS vs the energy.
"""
import numpy as np
import scipy

import matplotlib.pyplot as plt

# -- load Hamiltonian
H = scipy.sparse.load_npz('./hamiltonian.npz')
d = H.shape[0]

E = np.load('./energy.npy')
ids = np.load('./ids.npy')
dos = np.load('./dos.npy')

n = np.sum(dos) #* (E[1]-E[0])
dos = dos / n


np.savetxt('dos_64.dat', dos)
np.savetxt('energy_64.dat', E)

def kpm_loops(n):

    loops = []
    for i in range(n):
        if not i%2:
           loops.append(np.sum((E**i) * dos))
        
    return loops 

def exact_loops(n):
    """
        Calculates N_e(n) = <e| H^n |e> by applying H repeatetly to |e>
    """

    # -- vector corresponding to identity element
    v = np.zeros(d, dtype=complex)
    v[0] = 1

    loops = []
    for i in range(n):
        if not i%2:
           loops.append(v[0].real)
        v = H.dot(v)
        
    return loops


if __name__ == '__main__':


    # moments = [ moment(n) for n in range(20) ]
    
    # np.savetxt('kpm_moments.txt', moments)

    n = 20
    l1 = np.array(kpm_loops(n) )
    l2 = np.array(exact_loops(n) )

    print(exact_loops(n))

    plt.plot(np.abs((l1-l2)/l2),'o')
    plt.grid()
    ax = plt.gca()
    ax.set_yscale('log')
    plt.show()