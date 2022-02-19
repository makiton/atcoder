#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
s = next(tokens)
Xs = int(s)
if Xs > -10 and Xs < 0:
    print(-1)
    exit()
elif Xs < 10 and Xs >= 0:
    print(0)
    exit()

X = int(s[:-1])  # type: int
if X < 0 and s[-1] != '0':
    print(X-1)
else:
    print(X)
