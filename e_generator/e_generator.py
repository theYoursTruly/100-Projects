""" 
    E constant generator
    Generate e up to a specific digit.

    INPUT:
    1) precision - number of digits (after comma) to generate [NUMBER]

    OUTPUT:
    generated e
"""
from sys import argv
from math import e


def factorial(n):
    fac = 1;
    for i in range(n):
        fac *= i+1
    return fac

if __name__ == "__main__":
    # Parse and check input
    precision = -1
    if len(argv) > 1:
        try:
            precision = int(argv[1])
        except ValueError:
            pass

    if precision <= 0:
        print("Usage: e_generator <precision>\n    precision - number of digits (after comma) to generate [NUMBER; min: 1]")
    else:
        my_e = 2
        n = 1
        chunk = 1
        while chunk >= (10 ** (-precision)):
            n += 1
            chunk = 1 / factorial(n)
            my_e += chunk
            print(n, chunk, my_e)

        print("Calculated e: {1:.{0}}\nReal e:       {2:.{0}}".format(precision+1, my_e, e))
