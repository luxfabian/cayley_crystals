# Lifting topological models from their abelianization

We want to take a look at a proposed model on the hyperbolic disk which might display nontrivial second Chern numbers and which has been proposed recently in 

    Zhang, W., Di, F., Zheng, X. et al. Hyperbolic band topology with non-trivial second Chern numbers. Nat Commun 14, 1083 (2023). https://doi.org/10.1038/s41467-023-36767-8

Let $\mathcal{F}$ denote the Fuchsian group of order 2, given by the presentation

$$
\mathcal{F} = \langle \gamma_1, \gamma_2, \gamma_3, \gamma_4 ~|~ \gamma_1 \gamma_2^{-1}
 \gamma_3 \gamma_4^{-1} \gamma_1^{-1} \gamma_2 \gamma_3^{-1} \gamma_4 \rangle $$

Let $\sigma_j$, $j=1,2,3$ denote the Pauli matrices.
We define the Clifford matrices
$$
\Gamma_1 =  -\sigma_2 \otimes \sigma_1,\\ 
\Gamma_2 =  \sigma_1 \otimes \sigma_1, \\
\Gamma_3 =  \sigma_1 \otimes \sigma_2, \\
\Gamma_4 =  \sigma_1 \otimes \sigma_3, \\
\Gamma_5 =  \sigma_3 \otimes1, \\
$$
We define a Hamiltonian in the algebra $M_4(\mathbb{C})\otimes\mathbb{C}\mathcal{F}$ by
$$
H = \frac{1}{2i} \sum_{j=1}^4 t_j  \Gamma_j \otimes( \gamma_j - \gamma_j^{-1})
+ \Gamma_5 \otimes \left( m + \frac{1}{2} \sum_{j=1}^4 J_j ( \gamma_j + \gamma_j^{-1})\right) 
+ i a \Gamma_1 \Gamma_4 \otimes 1.
$$
The abelianization of $\mathcal{F}$ is given by
$$
\mathcal{F}_{\mathrm{ab}} = \mathcal{F} / [\mathcal{F},\mathcal{F}] \cong \mathbb{Z}^4 .
$$
Consider the map $\phi\colon  \mathcal{F} \to \mathcal{F}_{\mathrm{ab}}$ which sends $\mathcal{F}$ to its abelianization and which we extend to $M_4(\mathbb{C})\otimes\mathbb{C}\mathcal{F}$.
Let $T_i = \phi(\gamma_i)$, denote the discrete translation operators of $\mathbb{Z}^4$.
Then we obtain the image of $H$ as 
$$
\phi(H) = H_{\mathrm{ab}} = \frac{1}{2i} \sum_{j=1}^4 t_j \Gamma_j \otimes( T_j - T_j^{-1})
+ \Gamma_5 \otimes \left( m + \frac{1}{2} \sum_{j=1}^4 J_j ( T_j + T_j^{-1})\right)  + i a \Gamma_1 \Gamma_4 \otimes 1 .
$$
A Bloch-Floquet decomposition yields the momentum space Hamiltonian
$$
 H_k =  \sum_{j=1}^4 \Gamma_j  \sin(k_j)
+ \Gamma_5  \left( m + \sum_{j=1}^d \cos(k_j) \right) + a \Gamma_1 \Gamma_4  = d(k) \cdot \Gamma + a \Gamma_1 \Gamma_4,
$$
and where 
$$
d(k) = \left( t_1 \sin(k_1), t_2 \sin(k_2), t_3 \sin(k_3), m + \sum_{j=1}^d J_j \cos(k_j)) \right)^T .
$$
We only consider $t_j = J_j = 1$. For $m=0.7$ and $a=0.2$, the Dirac points in the spectrum are gapped for the abelianized Hamiltonian. But is this really the case for the hyperbolic lattice and the full Hamiltonian H?