import numpy as np


E = np.load('./energy.npy')
ids = np.load('./ids.npy')
dos = np.load('./dos.npy')

dos = dos / np.sum(dos)

def moment(n):

    return np.sum( (E**n) * dos )

if __name__=='__main__':

    for n in range(10):
        print(moment(n))