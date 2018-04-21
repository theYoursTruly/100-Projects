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
        my_pi = 0
        for n in range(precision):
            my_pi += ((1/16) ** n) * ((4 / (8*n + 1)) - (2 / (8*n + 4)) - (1 / (8*n + 5)) - (1 / (8*n + 6)))
        print("Calculated pi: {1:.{0}}\nReal pi:       {2:.{0}}".format(precision+1, my_pi, pi))
