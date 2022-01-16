#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"

b = A[0]
d = 0
cnt = 1
for a in A:
    if d > 0 and a-b < 0:
        cnt += 1
        d = 0
    elif d < 0 and a-b > 0:
        cnt += 1
        d = 0
    elif a - b != 0:
        d = a - b
    b = a

print(cnt)
