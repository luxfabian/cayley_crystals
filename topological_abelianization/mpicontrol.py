"""
   Summarizes many functionalieties of the  mpi4py package
   into a single class MPI.

   Implements different ways to assign work to MPI threads.

   Author: Fabian R. Lux
   Date:   11/12/22
"""

from mpi4py import MPI
import time
import sys
import numpy as np


class MPIControl:

    def __init__(self):

        # -- MPI communicator
        self.comm = MPI.COMM_WORLD

        # -- Index of the current MPI thread
        self.rank = self.comm.Get_rank()

        # -- Total number of active MPI threads
        self.size = self.comm.Get_size()

        # -- Default index (useful for tasks meant for one thread only)
        self.root = 0

        # -- Error code
        self.err = 0

        # -- Internal timing variables
        self._t0 = 0.0
        self._t1 = 0.0
        self._total = 0.0

    def finalize(self):
        """
            Concludes the MPI session
        """
        MPI.Finalize()

    def barrier(self):
        """
            Code execution resumes only after every MPI thread
            has reached the barrier
        """
        self.comm.Barrier()

    def start_clock(self):
        """
            Starts timing on root thread
        """
        if self.rank == self.root:
            self._t0 = time.time()

    def stop_clock(self):
        """
            Ends timing on root thread
        """
        if self.rank == self.root:
            self._t1 = time.time()
            self._total = self._t1 - self._t0

    def get_time(self):
        if self.rank == self.root:
            return self._total

    # -- printing -------------------------------------------------------

    def print(self, *args):
        if self.rank == self.root:
            # -- standard print if root
            print(*args)

            # -- necessary to keep streaming continously
            sys.stdout.flush()

    def is_root(self):
        """
            Returns true if the current rank is the root
        """
        return (self.rank == self.root)

    def my_turn(self, i, method='linear'):
        """
            Returns true if the current rank is assigned
            to job i
        """

        if method == 'linear':
            # -- cycle through ranks
            return (i % self.size) == self.rank

        if method == 'random':
            # -- ISO/IEC 9899 LCG
            a = 1103515245  # multiplier
            c = 12345  # increment
            m = 2**32  # modulus

            return ((a*i+c) % m) % self.size == self.rank

    # -- communication --------------------------------------------------

    def reduce_sum(self, arr, arr_red):

        # extract data type
        if arr.dtype == np.dtype(np.float64):
            type = MPI.DOUBLE
        elif arr.dtype == np.dtype(np.int32):
            type = MPI.INT
        else:
            self.print("MPI ERROR: unknown dtype")
            self.err = 1
            exit(-1)

        self.comm.Reduce(
            [arr, type],
            [arr_red, type],
            op=MPI.SUM,
            root=self.root
        )

    def broadcast(self, arr):
        return self.comm.bcast(arr, root=self.root)

    def gather(self, data):
        return self.comm.gather(data, root=self.root)

    # -- dynamic load balancing -----------------------------------------

    def assign_work(self, i):
        # find available worker unit
        worker_unit = self.comm.recv(source=MPI.ANY_SOURCE)
        # send some work to it
        self.comm.send(i, dest=worker_unit)

    def stop_working_units(self):
        for i in range(self.size - 1):
            worker_unit = self.comm.recv(source=MPI.ANY_SOURCE)
            self.comm.send(-1, dest=worker_unit)


def test_mpi():

    mpiv = MPIControl()

    print("A warm hello from: ", mpiv.rank, "/", mpiv.size)


if __name__ == '__main__':
    test_mpi()
