#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
M = int(next(tokens))  # type: int
X = sorted([int(next(tokens)) for _ in range(M)])  # type: "List[int]"

print(sum(sorted([X[i + 1] - X[i] for i in range(M - 1)], reverse=True)[N - 1 :]))
