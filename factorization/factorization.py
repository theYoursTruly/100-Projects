""" 
    Prime factorization
    Split a number into it's prime factors.

    INPUT:
    1) number - number to process [NUMBER]

    OUTPUT:
    Prime factors of the input number.
"""
from sys import argv

if __name__ == "__main__":
    # Parse and check input
    number = -1
    if len(argv) > 1:
        try:
            number = int(argv[1])
        except ValueError:
            pass

    if number <= 0:
        print("Usage: fibonacci <mode> <number>\n    {}\n    {}".format(
                "mode   - 1 to generate n-th number, 2 to check given number [NUMBER]",
                "number - number to check or calculate [NUMBER]"))
    elif number == 1:
        print("1: 1")
    else:
        print("{}: ".format(number), end="")
        div = 2
        while div <= (number ** 0.5):
            if number % div == 0:
                print(div, end=" ")
                number /= div
            else:
                div += 1
        print(int(number))
