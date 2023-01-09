# Spectral and Combinatorial Aspects of Cayley Crystals
Fabian R. Lux<sup>1</sup> and Emil Prodan<sup>1</sup><br />
<sup>1</sup>*Department of Physics and, Department of Mathematical Sciences, Yeshiva University, New York, NY 10016, USA*

DOI: [10.13140/RG.2.2.12735.59040](http://dx.doi.org/10.13140/RG.2.2.12735.59040)

This is a repository for code, related to our paper on the "Spectral and Combinatorial Aspects of Cayley Crystals".

## Abstract

Owing to their interesting spectral properties, the synthetic crystals over lattices other than regular Euclidean lattices, such as hyperbolic and fractal ones, have attracted renewed attention, especially from materials and meta-materials research communities. They can be studied under the umbrella of quantum dynamics over Cayley graphs of finitely generated groups. In this work, we investigate numerical aspects related to the quantum dynamics over such Cayley graphs. Using an algebraic formulation of the "periodic boundary condition" due to Lück [Geom. Funct. Anal. **4**, 455–481 (1994)], we devise a practical and converging numerical method that resolves the true bulk spectrum of the Hamiltonians. Exact results on the matrix elements of the resolvent, derived from the combinatorics of the Cayley graphs, give us the means to validate our algorithms and also to obtain new combinatorial statements. Our results open the systematic research of quantum dynamics over Cayley graphs of a very large family of finitely generated groups, which includes the free and Fuchsian groups.

## How to use the code

The code base is divided in two parts:

1. `./free_group`: Code related to the free group on two generators:

$$
\mathbb{F}_2 = \langle a,b\rangle .
$$

2. `./fuchsian_group`: Code related to the Fuchsian group of genus 2:

$$
\mathcal{F}_2  = \langle a_1 ,b_1, a_2,b_2 ~|~ [a_1,b_1][a_2, b_2] \rangle .
$$

A separate `README.md` file with further instructions can be found in each of the respective folders.
