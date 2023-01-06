# Fuchsian group of genus 2

This code studies the Fuchsian group of genus two and its finite, coherent approximations.

## Requirements

* `Python 3`
* `numpy`
* `matplotlib`


## Running the code

We mod w.r.t. $p^N$ in order to generate a finite approximation of the Fuchsian group with periodic boundary conditions. Both $p$ and $N$ can be specified in the input file `input.py`.

Run `python generate_group.py` in order to find the basis elements of the finite approximation. Then run `python spectrum.py` to compute the spectrum of the Hamiltonian as psrescribed in the manuscript. In order to visualize the integrated density of states, one can run `python post_processing.py`.
