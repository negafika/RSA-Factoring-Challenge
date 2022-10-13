#!/usr/bin/python3
import sys


def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if not n % 2:
        return 2
    if not n % 3:
        return 3
    i = 5
    stop = int(n ** 0.5)
    while i <= stop:
        if not n % i:
            return i
        if not n % (i+2):
            return i + 2
        i += 6
    return True


f = open(str(sys.argv[1]), "r")
for x in f:
    y = int(x)
    b = is_prime(y)
    print("{:d}={:d}*{:d}".format(y, y//b, b))
    f.close()
