"""
    ./py/post_process_bbh_model.py

    Author: Fabian R. Lux
    Date:   6/27/2023

    Post process
"""

import numpy as np

fsize_major= 18
fsize_minor= 12

import matplotlib.pyplot as plt
import matplotlib.colors as colors

prl_figure_width =1*(3 + 3/8) #inch

aspect = 1.2
golden_ratio = 1.61803398875

energy = np.load("./out/hyperbolic_chern_energy.npy")
dos = np.load("./out/hyperbolic_chern_dos.npy")   

fig=plt.figure(figsize=(aspect*prl_figure_width,prl_figure_width))


plt.plot(energy,dos)



plt.tight_layout()
plt.savefig('./out/hyperbolic_chern_dos.png',dpi=300)
# plt.show()
plt.clf()