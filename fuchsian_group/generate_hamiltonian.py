import json
import scipy

import input
from fuchsian import *

# --  initialize basis objects

with open('./lexikon.json', 'r') as file:
    json_data = json.load(file)

basis = [Fuchsian(word=f['word'], n=f['n'])%(input.p**input.N) for f in json_data]
d = len(basis)

hashed_basis = [b.hash for b in basis]

dict_basis = {}

for i in range(len(basis)):
    dict_basis[str(hashed_basis[i])] = i

def represent(op):
    """
        op: integer index of the operator in the basis
    """

    representation = scipy.sparse.lil_matrix((d, d), dtype=complex)
    for j in range(d):
        c = (op*basis[j]) % (input.p**input.N)

        i = dict_basis[str(c.hash)]

        representation[i, j] = 1

    return representation

def set_hamiltonian():
    """
        Construct the sparse Hamiltonian
    """
    H = scipy.sparse.csr_matrix((d, d), dtype=complex)
    H_operators = [ Fuchsian(word=[w]) for w in generators ]

    for g in H_operators:
        H += represent(g)

    print("Storing the hamiltionian to the file ./hamiltonian.npz ...")
    scipy.sparse.save_npz('./hamiltonian.npz', H, compressed=True)
    print("Done!")


if __name__ == "__main__":
    set_hamiltonian()


    