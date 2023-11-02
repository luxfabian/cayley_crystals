import numpy as np
import matplotlib.pyplot as plt

from input import *
spectrum = np.load('./spectrum.npy')


def IDS(spectrum, mu):

    return (spectrum < mu).sum() / len(spectrum)

def IDS_exact(mu):

    nu = 4

    ids = 0.0
    if mu < -2 * np.sqrt(nu-1):
        ids = 0.0
    elif  mu > 2 * np.sqrt(nu-1):
        ids = 1.0
    else:
        ids = 1/2 + nu/(2*np.pi) * (
            np.arcsin(mu/(2 * np.sqrt(nu-1)))
            - (nu-2)/nu * np.arctan((nu-2)*mu/ ( nu * np.sqrt(4*(nu-1) -mu**2)))
        )

    return ids


Es = np.linspace(-6, 6, 200)

IDS_dat_N = [IDS(spectrum, mu) for mu in Es]
IDS_dat_exact= [IDS_exact(mu) for mu in Es]


plt.plot(Es, IDS_dat_N, label=r'Numerical')
#plt.plot(Es, IDS_dat_exact, '--', label=r'$F(\mu)$')



plt.title(r'$N$={}, dim $H_N$={}'.format(N, len(spectrum)))

plt.legend()
ax = plt.gca()

ax.set_ylabel(r'IDS')
ax.set_xlabel(r'$\mu$')
#ax.set_ylim((0,1.4*exact_dos(4, eta)))
# ax.set_yscale('log')
ax.ticklabel_format(style='sci')
plt.tight_layout()

plt.savefig('./spectrum.png', dpi=300)
plt.show()
