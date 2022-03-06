#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
K = int(next(tokens))  # type: int


def f(n, k):
    if k < 2 or k > 2*n:
        return 0
    return min(k-1, 2*n+1-k)


ans = 0
for i in range(2, 2*N+1):
    ans += f(N, i) * f(N, i-K)

print(ans)
