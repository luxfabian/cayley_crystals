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


def convergence_vs_moments():

    moments = [2**n for n in range(1,10)]

    epsilon = 1e-4
    n_random_states=20

    (E,dos) = kpm.density_of_states(H, scale=8, n_moments=1, n_energies=300, kernel="jackson",
            n_random_states=n_random_states, epsilon = epsilon)

    ids_prev = IDS(E, dos)

    errors = []
    for n in moments:

        (E, dos) = kpm.density_of_states(H, scale=8, n_moments=n, n_energies=300, kernel="jackson",
            n_random_states=n_random_states, epsilon = epsilon)

        ids_next = IDS(E,dos)

        error = np.mean( (ids_prev - ids_next)**2 ) 
        errors.append(error)

        ids_prev = ids_next

        

    plt.plot(moments,errors,'o') # plot this dos

    #plt.title(r'Kernel polynomial method for $p=2$, $N=6$ and $p^N=64$')
    ax = plt.gca()
    ax.set_xlabel(r'No. of Chebyshev moments')
    ax.set_ylabel(r'Mean sq. convergence of IDS')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.grid()
    plt.savefig('./error_vs_moments.png', dpi=300)
    plt.show()


def convergence_vs_random_vecs():

    n_moments = 256

    epsilon = 1e-4

    n_random_states= [5,10,20,50,100,200]

    (E,dos) = kpm.density_of_states(H, scale=8, n_moments=n_moments, n_energies=300, kernel="jackson",
            n_random_states=1, epsilon = epsilon)

    ids_prev = IDS(E, dos)

    errors = []
    for n in n_random_states:

        (E, dos) = kpm.density_of_states(H, scale=8, n_moments=n_moments, n_energies=300, kernel="jackson",
            n_random_states=n, epsilon = epsilon)

        ids_next = IDS(E,dos)

        error = np.mean( (ids_prev - ids_next)**2 ) 
        errors.append(error)

        ids_prev = ids_next

        

    plt.plot(n_random_states,errors,'o') # plot this dos

    #plt.title(r'Kernel polynomial method for $p=2$, $N=6$ and $p^N=64$')
    ax = plt.gca()
    ax.set_xlabel(r'No. of random states')
    ax.set_ylabel(r'Mean sq. convergence of IDS')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.grid()
    plt.savefig('./error_vs_states.png', dpi=300)
    plt.show()




if __name__ == "__main__":
    convergence_vs_moments()
    convergence_vs_random_vecs()

