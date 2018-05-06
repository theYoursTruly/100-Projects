""" 
    Prime finder
    Find prime numbers until a user stops asking for one.
    First number truly searched for is 3.

    INPUT:
    Interactive: y to generate next prime, n to quit

    OUTPUT:
    Next prime number
"""

primes = [2]
candidate = 1

def is_prime(n):
    for prime in primes:
        if prime <= (candidate ** 0.5):
            if (candidate % prime) == 0:
                return False
    return True


if __name__ == "__main__":
    char = 'y'
    while char == 'y':
        char = input('Generate next prime? [y/n] ')
        if char in ['y', 'n']:
            if char == 'y':
                candidate += 2
                while not is_prime(candidate):
                    candidate += 2
                print('Next prime:', candidate)
                primes.append(candidate)
        else:
            char = 'y'
