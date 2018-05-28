""" 
    Change calculator
    Shows what change and in what coins should be given, based on cost and provided currency.

    INPUT:
    1) cost - sum of all  the cost user is trying to cover [NUMBER]
    2) pay  - money provided to cover the cost [NUMBER]

    OUTPUT:
    Next prime number
"""
from sys import argv

if __name__ == "__main__":
    # Parse and check input
    cost = -1
    pay  = -1
    if len(argv) > 2:
        try:
            cost = float(argv[1])
            pay  = float(argv[2])
        except ValueError:
            pass

    if cost <= 0 or pay <= 0:
        print("Usage: change <cost> <pay>\n  Where pay >= cost.")
    else:
        # values of all the bills from biggest to lowest
        currency = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
        change = int(100 * (pay - cost))
        for bill in currency:
            print("Number of {0}: {1}".format(
                "${0} bills".format(bill) if bill >= 1 else "{0}c coins".format(bill),
                change // int(100 * bill)
            ))
            change %= int(100 * bill)
