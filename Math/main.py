from Class import Fraction


def AfficheFraction(F: Fraction):
    """
    Cette méthode affiche à l'utilisateur la fonction passée en paramètre sous la forme n / d
    """
    F.Afficher()


def ReduceFraction(F: Fraction) -> Fraction:
    """
    Cette fonction réduit la fraction donnée en paramètre et l'affiche
    """
    return F.Simplifier()


def SaisieFraction() -> Fraction:
    """
    Cette Fonction permet à l'utilisateur de saisir une fraction en rentrant dans l'ordre le numérateur et le
    dénominateur
    """
    n = int(input("Saisissez le numérateur "))
    d = int(input("Saisissez le dénominateur "))
    if n == 0:
        F = Fraction(0, 1)
    else:
        if (n * d) > 0:
            F = Fraction(abs(n), abs(d))
        else:
            F = Fraction(-1 * abs(n), abs(d))
    return F


def Multiplication(F0: Fraction, F1: Fraction):
    """
    Cette fonction multiplie les fractions rentrées en paramètre puis renvoie le résultat sur la forme d'une fraction
    simplifiée
    """
    nouvnum = F0.getNumerator() * F1.getNumerator()
    nouvdenom = F0.getDenominator() * F1.getDenominator()
    F = Fraction(nouvnum, nouvdenom)
    F.Simplifier()
    return F


def MemeDenominator(F0: Fraction, F1: Fraction):
    """
    Cette fonction met au même dénominateur deux fonctions et les renvoie
    """
    den = int(F0.getDenominator() * F1.getDenominator())  # den correspond au dénominateur commun
    F2 = Fraction(F0.getNumerator() * F1.getNumerator(), den)
    F3 = Fraction(F0.getNumerator() * F1.getNumerator(), den)
    return F2, F3


def Addition(F0: Fraction, F1: Fraction):
    """
    Cette fonction renvoie la somme de deux fractions sous la forme d'une autre fraction
    """
    F0, F1 = MemeDenominator(F0, F1)

    F = Fraction((F0.getNumerator() + F1.getNumerator()), F0.getDenominator())
    F.Simplifier()
    return F


def Soustraction(F0: Fraction, F1: Fraction) -> Fraction:
    """
    Cette fonction renvoie la différence de deux	fractions sous la forme d'une autre fraction
    La deuxième fraction rentrée soustrait la première.
    """
    F0, F1 = MemeDenominator(F0, F1)
    F = Fraction(F0.getNumerator() - F1.getNumerator(), F0.getDenominator())
    return F


def Inverser(F: Fraction) -> Fraction:
    """
    Cette fonction inverse la fonction rentrer en paramètre
    """
    f = Fraction(F.getDenominator(), F.getNumerator())
    f.Simplifier()
    return f


def Carre(F: Fraction) -> Fraction:
    """
    Cette Fonction renvoie le carré réduit de celle rentrée en paramètre
    """
    F = Multiplication(F, F)
    F.Simplifier()
    return F
