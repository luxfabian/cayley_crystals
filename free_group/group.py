"""
    ./free_group/group.py

    Author: Fabian R. Lux
    Mail:  fabian.lux@yu.edu

    Implements basic group structure of the free group.
    a,b are the generators; A,B their resp. inverses.
"""
import numpy as np


# -- basic group elements
e = np.array([[1,0],[0,1]], dtype=int)
a = np.array([[1, 2], [0, 1]], dtype=int)
b = np.array([[1, 0], [2, 1]], dtype=int)
A = np.array([[1, -2], [0, 1]], dtype=int)
B = np.array([[1, 0], [-2, 1]], dtype=int)

# generators =  np.array( [a,b,A,B] , dtype=int)
generators =  np.array( [a,b] , dtype=int)


def mult(h,g,N):
    """
        Matrix multiplication modulo N
    """
    return np.dot(h,g) % N

def encode(x):
    """
        Hash representation of x
    """
    return hash(str(x))
