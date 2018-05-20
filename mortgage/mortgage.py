""" 
    Mortgage calculator
    Calculate payments and montly payments of the mortgage.

    INPUT:
    1) principal - initial amount of the loan [NUMBER]
    2) interest - interest rate of the loan [NUMBER]
    3) length - length (in years) of the mortgage [NUMBER]
    4) term - compounding interval (M - monthly, W - weekly, D - daily) [CHARACTER]

    OUTPUT:
    Payments for each term.
"""
from sys import argv
from math import pi

if __name__ == "__main__":
    # Parse and check input
    principal = -1
    interest = -1
    length = -1
    term = 'M'
    if len(argv) > 4:
        try:
            principal = int(argv[1])
            interest = float(argv[2])
            length = int(argv[3])
            term = argv[4]
        except ValueError:
            pass

    if principal <= 0:
        print("Principal must be a positive number")
    elif interest <= 0 or interest > 100:
        print("Interest (in %) must be between 1 and 100")
    elif length < 1:
        print("Length (in years) must be at least 1")
    elif term not in ['M', 'W', 'D']:
        print("Interval must be one of: M, W, D\n  M - monthly\n  W - weekly\n  D - daily")
    else:
        compounds = [12, 52, 355][['M', 'W', 'D'].index(term)]
        intervals = length * compounds
        interest = interest / (100 * compounds)
        payment = (interest * principal) / (1 - (1 + interest)**-intervals)

        print("Monthly payment:", round(payment*compounds/12, 2))
