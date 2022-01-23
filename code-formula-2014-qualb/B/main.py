#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = next(tokens)  # type: str

sums = [0, 0]
idx = 1
for n in reversed(list(N)):
    sums[idx] += int(n)
    idx ^= 1

print(' '.join(map(str, sums)))
