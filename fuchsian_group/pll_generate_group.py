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
from multiprocessing.dummy import Pool

import input
from fuchsian import *

n_threads = 96*2*2*2

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

        next_generation = []

        prev_generation_local = np.array_split(prev_generation, n_threads)

        def candidates(prev_generation_local):

            candidates_local = []
            hashed_lexikon_local  = hashed_lexikon.copy()

            for b in prev_generation_local:
                for g in generators:
                    candidate = (g*b) % denominator

                    # -- check if result is known
                    if candidate.hash not in hashed_lexikon_local:
                        # -- if not, add to lexikon
                        hashed_lexikon_local.add(candidate.hash)

                        # -- and keep track of the latest generation
                        candidates_local.append(candidate)

            return np.array( candidates_local )
        
        print("Entering the multi-threading region")
        with Pool(n_threads) as p:
            candidates_local = p.map(candidates, prev_generation_local)
        print("Exiting the multi-threading region")

        candidates = np.concatenate(candidates_local)
        hashes = np.array( [c.hash for c in candidates] )
        _, unique     = np.unique( hashes, return_index=True )

        next_generation =  candidates[unique]
        next_hashes =  hashes[unique]

        lexikon = np.append(lexikon, next_generation, axis=0)
        hashed_lexikon.update(next_hashes)


        

        
        #print(lexikon)

        # collection = set()
        # next_generation =  []
        # for candidate in candidates:
        #     if candidate.hash not in collection:
        #         # -- if not, add to lexikon
        #         lexikon = np.append(lexikon, [candidate], axis=0)
        #         hashed_lexikon.add(candidate.hash)

        #         collection.add(candidate.hash)

        #         # -- and keep track of the latest generation
        #         next_generation.append(candidate)


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

    print("Welcome!")

    impose_periodic_boundary_condition(input.p**input.N)