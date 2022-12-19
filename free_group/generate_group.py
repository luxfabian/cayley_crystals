"""
    ./free_group/generate_group.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Finds a finite approximation for the free group on two generators.
    As described in the paper, we simply mod out.

    The modding occurs with respect to input.p ** input.N.

    The resulting basis objects are stored in binary format to ./lexikon.npy
"""
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt

import input
from group import *


def elementQ(x, hashed_basis):
    """
        Check if x is known 
    """

    h = encode(x)

    return h in hashed_basis


lexikon = np.array([e])
hashed_lexikon = {encode(x) for x in lexikon}
n_words = len(lexikon)

prev_generation = np.array([e])
lens = []
count = 1

print("gen\t | words")
while True:

    print(count, '\t |', n_words)
    lens.append(n_words)

    it = 0

    next_generation = []

    for b in prev_generation:

        ct = 0
        for g in generators:
            candidate = mult(b, g, input.p ** input.N)

            # -- check if result is known
            if not elementQ(candidate, hashed_lexikon):
                # -- if not, add to lexikon
                lexikon = np.append(lexikon, [candidate], axis=0)
                hashed_lexikon.add(encode(candidate))

                # -- and keep track of the latest generation
                next_generation.append(candidate)

    if len(lexikon) == n_words:
        break
    else:
        n_words = len(lexikon)
        prev_generation = next_generation
        count += 1


np.save('./lexikon.npy', lexikon)

plt.plot(lens, 'o')

plt.title(
    r"Iterative factor group generation $M_2(\mathbb{Z}/p^n\mathbb{Z})$ with p="
    + str(input.p)
    + " and N="
    +str(input.N)
)

ax = plt.gca()


ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

ax.set_xlabel("generation")
ax.set_ylabel("basis elements")

plt.tight_layout()
plt.savefig('./basis_search.png', dpi=300)
# plt.show()
