######################################################################################################################
# Name:         Josephine Rei Sale
# Date:         1-5-2022
# Description:  A program that accepts and modifies functions.
######################################################################################################################

# the fraction class
class Fraction:
    def __init__ (self, num = 0, den = 1): 
        self.num = num
        if den == 0:        # no dividing by 0
            self.den = 1
        else:
            self.den = den

        self.dec = (self.num / self.den)

    @property 
    def num (self):
        return self._num
    @num.setter
    def num (self, value):
        self._num = value

    @property 
    def den (self):
        return self._den
    @den.setter
    def den (self, value):
        if int (value) != 0:        # I mean it. no / 0
            self._den = value

    def __str__(self):
        return f"{self.num} / {self.den} ({self.dec}) "

    def reduce(self):
        gcd = 1
        minumum = min(abs(self.num), abs(self.den))

        for i in range(2, int(minumum) + 1):
            if self.num % i == 0 and self.den % i == 0:
                gcd = i

        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)

        if self.num == 0:       # 0 = 0 = 0.
            self.den = 1        # therefore, 1 is simplest den

    def __add__(self, other):       # common den & add
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        result = Fraction(num, den)
        result.reduce()
        return result

    def __sub__(self, other):       # common den & subtract
        num = self.num * other.den - self.den *other.num
        den = self.den * other.den
        result = Fraction (num, den)
        result.reduce()
        return result

    def __mul__(self, other):       # just multiply straight
        num = self.num * other.num
        den = self.den * other.den
        result = Fraction (num, den)
        result.reduce()
        return result

    def __truediv__ (self, other):      # flip the second, then multiply
        num = self.num * other.den
        den = self.den * other.num
        result = Fraction (num, den)
        result.reduce()
        return result





# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print()
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)
