# Free group

This code studies the free group on two generators:
$$
\mathbb{F}_2 = \langle a,b\rangle ,
$$
and its finite, coherent approximations.

## Requirements

* `Python 3`
* `numpy`
* `matplotlib`


## Running the code

We mod w.r.t. $p^N$ in order to generate a finite approximation of the free group on two generators with periodic boundary conditions. Both $p$ and $N$ can be specified in the input file `input.py`.

Run `python generate_group.py` in order to find the basis elements of the finite approximation. Then run `python spectrum.py` to compute the spectrum of the Hamiltonian as prescribed in the manuscript. In order to visualize the integrated density of states, one can run `python post_processing.py`.