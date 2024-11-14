"""
Module main pour nous exercer sur les fonctions en language python.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Permet de dire si le nombre p mit en paramètre est un nombre premier.

    Args : 
        n : nombre à tester

    Return :
        True si n premier
        False si n non premier
    """
    premier = True
    rc = int(sqrt(p))
    if p == 1 :
        premier = False
    for d in range (2,rc + 1):
        if p % d == 0:
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    Permet de tester la fontion isprime()
    """
    isprime(5)

    isprime(7)

    isprime(30  )

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
