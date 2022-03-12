#!/usr/bin/env python3
from functools import lru_cache
import math
import sys

MOD = 998244353  # type: int


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
X = int(next(tokens))  # type: int


@lru_cache
def solve(n):
    if n <= 4:
        return n
    return solve(n // 2) * solve((n+1)//2) % MOD


print(solve(X))
