""" 
    Fibonacci generator
    Generate n-th fibonacci number or check if a number belongs to the fibonnaci sequence.

    INPUT:
    1) mode   - 1 to generate n-th number, 2 to check given number [NUMBER]
    2) number - number to check or calculate [NUMBER]

    OUTPUT:
    mode 1: n-th fibonacci number
    mode 2: True if a number belongs to fibonacci sequence, False otherwise
"""
from sys import argv

if __name__ == "__main__":
    # Parse and check input
    mode = -1
    number = -1
    if len(argv) > 2 and argv[1] in ('1', '2'):
        try:
            mode = int(argv[1])
            number = int(argv[2])
        except ValueError:
            pass

    if mode <= 0 or mode > 2 or number < 0:
        print("Usage: fibonacci <mode> <number>\n    {}\n    {}".format(
                "mode   - 1 to generate n-th number, 2 to check given number [NUMBER]",
                "number - number to check or calculate [NUMBER]"))
    else:
        if mode == 1:
            fib0 = 0
            fib1 = 1
            for n in range(number):
                fib_next = fib0 + fib1
                fib0 = fib1
                fib1 = fib_next
            print("Calculated fibonacci number: {}".format(fib0))
        else:
            square1 = (5 * (number ** 2) + 4) ** 0.5
            square2 = (5 * (number ** 2) - 4) ** 0.5
            is_fib = square1.is_integer() or square2.is_integer()

            print("Number {} is {}a fibonacci number.".format(number, "" if is_fib else "not "))
