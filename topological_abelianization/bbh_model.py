"""
    ./scripts/bbh_model.py

    Author: Fabian R. Lux
    Date:   2023-06-27

    Benalcazar-Bernevig-Hughes model on the {p,q} Cayley crystal. See:

    [1] https://doi.org/10.48550/arXiv.2305.04945
    [2] https://doi.org/10.1126/science.aah6442
"""

# -- options -----------------------------

h0 = 1.5 #A-coupling
h1 = 0.5 #B-coupling
n_energies = 500
n_moments = 100
n_random_states = 20

# ----------------------------------------

import iomodule
import kpm
import scipy
import numpy as np
from scipy.sparse import lil_matrix

import matplotlib.pyplot as plt
import matplotlib.colors as colors

plt.rcParams.update({'font.size': 14})

access_point = iomodule.get_access_point()

print("Projector interpolation")
print(access_point)

projectors = ["A", "B"]
orders     = [access_point['p'], access_point['q']]

generators = [ "A", "iA", "B", "iB" ,"AB"]

d = access_point['d']

# -- initialize the matrices
g  = {}
g['A']  = lil_matrix((d,d))
g['iA'] = lil_matrix((d,d))
g['B']  = lil_matrix((d,d))
g['iB'] = lil_matrix((d,d))
g['AB'] = lil_matrix((d,d))

fname_prefix = access_point['fprefix']
for k in generators:
    reg_fname = fname_prefix + "_" + k + ".reg" 
    reg_data  = np.loadtxt(reg_fname, dtype=int, delimiter=" ")

    for [i,j] in reg_data:
        g[k][i,j] += 1.0

def bbh_hamiltonian(h0, h1):

    # -- BBH Hamiltonian
    H = h1 * (g['A'] + g['iA']) + h0 * (g['B'] + g['iB'])

    return H


H = bbh_hamiltonian(h0, h1)

energy, dos = kpm.density_of_states(H, scale=5, n_moments=n_moments, n_energies=n_energies, n_random_states=n_random_states)

np.save("./out/BBH_energy.npy", energy)
np.save("./out/BBH_dos.npy", dos)       
