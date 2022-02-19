#!/usr/bin/env python3
import sys
import math


def eratosthenes(n):
    list_prime = list(range(2, n))

    for i in range(2, n):
        if i in list_prime:
            for j in range(i * 2, n, i):
                if j in list_prime:
                    list_prime.remove(j)

        if i > int(math.sqrt(n)):
            break

    return list_prime


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
A = int(next(tokens))  # type: int
B = int(next(tokens))  # type: int
C = int(next(tokens))  # type: int
D = int(next(tokens))  # type: int

primes = eratosthenes(B+D+1)

for a in range(A, B+1):
    flg = False
    for b in range(C, D+1):
        if (a + b) in primes:
            flg = True
            break
    if not flg:
        print("Takahashi")
        exit()

print("Aoki")
