"""
    ./fuchsian_group/fuchsian.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Defines a faithful representation of the Fuchsian group of genus 2 in accordnace with the work of
    Maskit, Proc. Am. Math. Soc. 127 3643-3652 (1999).
"""
import numpy as np
from field import F

Γ = {}

generators = ['a₁', 'a₂', 'b₁', 'b₂', 'a₁⁻¹', 'a₂⁻¹', 'b₁⁻¹', 'b₂⁻¹']
inverse_generators = ['a₁⁻¹', 'a₂⁻¹', 'b₁⁻¹', 'b₂⁻¹', 'a₁', 'a₂', 'b₁', 'b₂']

Γ["e"] = np.array(
    [[F(1, 0), F(0, 0)], [F(0, 0), F(1, 0)]], dtype='object'
)

Γ['a₁'] = np.array(
    [[F(2, 2), F(-3, 0)],
     [F(3, 0), F(2, -2)]],
    dtype='object'
)

Γ['a₂'] = np.array(
    [[F(2, 0), F(-3, -2)],
     [F(3, -2), F(2, 0)]],
    dtype='object'
)

Γ['b₁'] = np.array(
    [[F(2, 0), F(0, -1)],
     [F(0, -1), F(2, 0)]],
    dtype='object'
)

Γ['b₂'] = np.array(
    [[F(-2, 2), F(-6, -3)],
     [F(6, -3), F(-2, -2)]],
    dtype='object'
)

Γ['a₁⁻¹'] = np.array(
    [[F(2, -2), F(3, 0)],
     [F(-3, 0), F(2, 2)]],
    dtype='object'
)

Γ['a₂⁻¹'] = np.array(
    [[F(2, 0), F(3, 2)],
     [F(-3, 2), F(2, 0)]],
    dtype='object'
)

Γ['b₁⁻¹'] = np.array(
    [[F(2, 0), F(0, 1)],
     [F(0, 1), F(2, 0)]],
    dtype='object'
)

Γ['b₂⁻¹'] = np.array(
    [[F(-2, -2), F(6, 3)],
     [F(-6, 3), F(-2, 2)]],
    dtype='object'
)


class Fuchsian():

    def __init__(self, word=None, mat=None, n=None):

        if word is None:
            self.word = ['e']
        else:
            self.word = word

        if mat is None:
            self.mat = self.parse_word()
        else:
            self.mat = mat

        if n is None:
            self.n = [self.word.count(g) for g in generators]
        else:
            self.n = n

        self.encode()
        self.reduce()

    def __repr__(self):
        return ''.join(self.word)

    def reduce(self):
        """
            Given a word it finds its full reduction
        """

        nw = len(self.word)

        i = 0
        end_of_word = False

        reduced_word = []
        while not end_of_word:
            # -- if not the last element
            if i < nw - 1:

                if self.word[i] != 'e':

                    id_g = generators.index(self.word[i])

                    if self.word[i+1] != inverse_generators[id_g]:
                        reduced_word.append(self.word[i])
                        i += 1
                    else:
                        i += 2

                else:
                    i += 1
            else:
                if i < nw and self.word[i] != 'e':
                    reduced_word.append(self.word[i])
                end_of_word = True

        if len(reduced_word) == 0:
            reduced_word.append('e')

        self.word = reduced_word

    def encode(self):
        self.hash = hash(str(self.mat))

    def parse_word(self):

        mats = [Γ[w] for w in self.word]

        if len(mats) > 1:
            return np.linalg.multi_dot(mats)
        else:
            return mats[0]

    def __mul__(self, other):

        word = self.word + other.word
        mat = np.dot(self.mat, other.mat)

        return Fuchsian(word, mat)

    def __mod__(self, k):

        word = self.word
        mat = self.mat % k

        return Fuchsian(word, mat)

    def __eq__(self, other):
        return self.hash == other.hash

    def dict(self):

        dictionary = {}

        dictionary['word'] = self.word
        dictionary['n'] = self.n

        return dictionary

    def load_dict(dict):

        pass


if __name__ == '__main__':

    w = ["a₁",  "a₁⁻¹", "b₁⁻¹", "b₁", ]

    F = Fuchsian(w)

    print(F)
    F.reduce()
    print(F)
    print(F.__dict__)

    print(F.json())
