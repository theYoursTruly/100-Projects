""" 
    Binary-Decimal Converter
    Converts given numbers between binary and decimal format.

    INPUT:
    1) number - input positive number in decimal or binary format [NUMBER]
    2) mode - B to convert to binary or D for decimal conversion [CHARACTER]

    OUTPUT:
    Converted number.
"""
from sys import argv


# -1 indicates error
def to_bin(str_in):
    result = ""
    try:
        number = int(str_in)
    except ValueError:
        return -1
    while number > 1:
        result = str(number % 2) + result
        number = number // 2
    result = str(number % 2) + result
    return result

# -1 indicates error
def to_dec(str_in):
    result = 0
    for i in range(len(str_in)):
        try:
            digit = int(str_in[i])
        except ValueError:
            return -1

        result += digit * 2**(len(str_in)-i-1)
    return result

if __name__ == "__main__":
    # Parse and check input
    mode = ""
    if len(argv) > 2:
        mode = argv[2]

    if mode not in ["B", "D"]:
        print("Usage: bin_dec <number> <mode>\n  Where: mode is B to convert to binary or D to convert to decimal")
    else:
        result = to_bin(argv[1]) if mode == "B" else to_dec(argv[1])
        if result == -1:
            print("Usage: bin_dec <number> <mode>\n  Invalid number given")
        else:
            print(result)