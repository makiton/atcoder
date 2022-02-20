#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
K = int(next(tokens))  # type: int

ans = K
for _ in range(N-1):
    ans *= K-1

print(ans)
