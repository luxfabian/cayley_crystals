"""
    ./fuchsian/post_processing.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Loads the spectrum. from ./spectrum.npy and computes the IDS.
"""
import numpy as np
import matplotlib.pyplot as plt

import input
spectrum = np.load('./spectrum.npy')


def IDS(spectrum, mu):

    return (spectrum < mu).sum() / len(spectrum)


Es = np.linspace(-6, 6, 200)

IDS_dat_N = [IDS(spectrum, mu) for mu in Es]

plt.plot(Es, IDS_dat_N, label=r'Numerical')

plt.title(f'$p$={input.p}, $N$={input.N}, dim $H_N$={len(spectrum)}')

plt.legend()
ax = plt.gca()

ax.set_ylabel(r'F(x)')
ax.set_xlabel(r'$x$')
ax.ticklabel_format(style='sci')
plt.tight_layout()

plt.savefig('./spectrum.png', dpi=300)
plt.show()
