"""
    ./free_group/post_processing.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Loads the spectrum. from ./spectrum.npy and computes the IDS.
    A comparison is made with known exact results.
"""
import numpy as np
import matplotlib.pyplot as plt

import input
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
plt.plot(Es, IDS_dat_exact, '--', label=r'Exact')



plt.title(f'$p$={input.p}, $N$={input.N}, dim $H_N$={len(spectrum)}')

plt.legend()
ax = plt.gca()

ax.set_ylabel(r'F(x)')
ax.set_xlabel(r'$x$')
ax.ticklabel_format(style='sci')
plt.tight_layout()

plt.savefig('./spectrum.png', dpi=300)
plt.show()
