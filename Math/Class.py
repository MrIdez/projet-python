from math import gcd


class Fraction:
    def __init__(self, numerator: float, denominator: float):
        assert denominator != 0, 'Le dénominateur de dois pas être nul'
        self.numerator = numerator
        self.denominator = denominator

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def Simplifier(self):
        p = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // p
        self.denominator = self.denominator // p

    def Afficher(self):
        print(self.numerator)
        print('-')
        print(self.denominator)
