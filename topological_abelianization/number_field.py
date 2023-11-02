import numpy as np

class Z3():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):

        if self.b==0:
            return str(self.a)
        elif self.a == 0:
            if self.b==1:
                return '√3'
            else:
                return str(self.b)+ '√3'
        else:
            if self.b==1:
                return '('+ str(self.a) + ' + √3)'
            else:
                return '('+ str(self.a) + ' + ' + str(self.b) + '√3)'
            

    def __mul__(self, other):

        a = self.a * other.a + 3 * self.b * other.b
        b = self.a * other.b + self.b * other.a

        return Z3(a,b)

    def __add__(self, other):
        return Z3(self.a + other.a, self.b + other.b)

    def __mod__(self, k):
        return Z3(self.a % k, self.b % k)

if __name__=='__main__': 


    F = Z3(1,3)


    print(Z3(0,1), "x", Z3(0,1), "=", Z3(0,1)*Z3(0,1))