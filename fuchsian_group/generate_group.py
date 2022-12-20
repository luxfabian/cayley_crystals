"""
    ./fuchsian_group/fuchsian.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Defines the Fuchsian group of genus 2 according following the work of
    Maskit, Proc. Am. Math. Soc. 127 3643-3652 (1999).
"""
import json
import numpy as np
import matplotlib.pyplot as plt

import input
from fuchsian import *

generator_labels = generators

generators = [Fuchsian([w]) for w in generator_labels]

# -- identity element
e = Fuchsian(['e'])


def impose_periodic_boundary_condition(denominator):

    # -- initialize the lexikon
    lexikon = np.array([e])
    hashed_lexikon = {x.hash for x in lexikon}
    n_words = len(lexikon)

    # -- keep track of the last generation that has been created
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
                candidate = (g*b) % denominator

                # -- check if result is known
                if candidate.hash not in hashed_lexikon:
                    # -- if not, add to lexikon
                    lexikon = np.append(lexikon, [candidate], axis=0)
                    hashed_lexikon.add(candidate.hash)

                    # -- and keep track of the latest generation
                    next_generation.append(candidate)

        if len(lexikon) == n_words:
            break
        else:
            n_words = len(lexikon)
            prev_generation = next_generation
            count += 1

    # -- save entire lexikon to file
    with open('./lexikon.json', 'w') as file:
        json.dump([lexikon[i].dict() for i in range(len(lexikon))], file)

    plt.plot(lens, 'o')

    plt.title(
        r"Iterative factor group generation $M_2(\mathbb{Z}/p^N\mathbb{Z})$ with p="
        + str(input.p)
        + " and N="
        + str(input.N)
    )

    ax = plt.gca()

    from matplotlib.ticker import MaxNLocator

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlabel("generation")
    ax.set_ylabel("basis elements")

    plt.tight_layout()
    plt.savefig('./basis_search.png', dpi=300)


if __name__ == '__main__':

    impose_periodic_boundary_condition(input.p**input.N)