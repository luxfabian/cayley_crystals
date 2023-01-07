"""
    ./fuchsian_group/field.py

    Author: Fabian R. Lux
    Date:   12/19/2022
    Mail:   fabian.lux@yu.edu

    Adjoins the square root of three to the field of integers.
"""

import numpy as np


class F():

    def __init__(self, a, b):
        # -- Z
        self.a = a
        # -- Z √3
        self.b = b

    def __repr__(self):
        """
            Pretty printing of the number
        """

        if self.b == 0:
            return str(self.a)
        elif self.a == 0:
            if self.b == 1:
                return '√3'
            else:
                return str(self.b) + '√3'
        else:
            if self.b == 1:
                return '(' + str(self.a) + ' + √3)'
            else:
                return '(' + str(self.a) + ' + ' + str(self.b) + '√3)'

    def __mul__(self, other):
        """
            Multiplication operator
        """

        a = self.a * other.a + 3 * self.b * other.b
        b = self.a * other.b + self.b * other.a

        return F(a, b)

    def __add__(self, other):
        """
            Addition operator
        """
        return F(self.a + other.a, self.b + other.b)

    def __mod__(self, k):
        """
            Modulo operator
        """
        return F(self.a % k, self.b % k)

    def __eq__(self, other):
        """
            Equality operator
        """
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        """
            Inequality operator
        """
        return self.a != other.a or self.b != other.b

    def __float__(self):
        """
            Conversion to float
        """
        return float(self.a + self.b * np.sqrt(3))


if __name__ == '__main__':

    """
        Some examples
    """

    print(F(0, 1), 'x', F(0, 1), '=', F(0, 1)*F(0, 1))

    print(F(0, 1), '=', float(F(0, 1)))

    print(F(0, 1) != F(0, 2))
