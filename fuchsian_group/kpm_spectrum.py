import scipy
import numpy as np
import matplotlib.pylab as plt

import kpm

# -- load Hamiltonian
H = scipy.sparse.load_npz('./hamiltonian.npz')

def IDS(E, dos):
    """
        Calculates the integrated density of states from the DOS.
        Uses the trapezoidal rule on the energy mesh defined by E.
    """

    # -- numerical integration of DOS
    ids = np.cumsum(dos)
    ids = scipy.integrate.cumulative_trapezoid(dos, E, initial=0)

    # -- normalization
    ids = ids / ids[-1]

    return ids


def spectrum():

    n_moments = 256
    epsilon = 1e-4
    n_random_states=50
    n_energies = 1000

    (E,dos) = kpm.density_of_states(H, scale=8, n_moments=n_moments, n_energies=n_energies, kernel="jackson",
            n_random_states=n_random_states, epsilon = epsilon)

    ids = IDS(E, dos)

    plt.plot(E,ids)
    plt.title(r'Kernel polynomial method for $p=2$, $N=6$ and $p^N=64$')
    ax = plt.gca()
    ax.set_xlabel(r'$\mu$')
    ax.set_ylabel(r'IDS($\mu$)')
    plt.grid()
    plt.savefig('./spec.png', dpi=300)
    plt.show()

    np.save('./energy.npy', E)
    np.save('./ids.npy', ids)
    np.save('./dos.npy', dos)


if __name__ == "__main__":
    spectrum()
    