"""
    ./fuchsian_group/kpm_moments.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Loads the KPM DOS from file and calculates the first moments of the
    DOS vs the energy.
"""
import numpy as np


E = np.load('./energy.npy')
ids = np.load('./ids.npy')
dos = np.load('./dos.npy')

dos = dos / np.sum(dos)


def moment(n):

    return np.sum((E**n) * dos)


if __name__ == '__main__':

    for n in range(10):
        print(moment(n))
