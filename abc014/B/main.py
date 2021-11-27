#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()

n = int(next(tokens))  # type: int
X = int(next(tokens))  # type: int
a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"

total = 0
i = 0
while X > 0:
    if X & 1:
        total += a[i]
    X >>= 1
    i += 1

print(total)
