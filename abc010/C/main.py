#!/usr/bin/env python3
import sys
import math

YES = "YES"  # type: str
NO = "NO"  # type: str


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
tx_a = int(next(tokens))  # type: int
ty_a = int(next(tokens))  # type: int
tx_b = int(next(tokens))  # type: int
ty_b = int(next(tokens))  # type: int
T = int(next(tokens))  # type: int
V = int(next(tokens))  # type: int
n = int(next(tokens))  # type: int
x = [int()] * (n)  # type: "List[int]"
y = [int()] * (n)  # type: "List[int]"
avail_range = T*V
for i in range(n):
    x[i] = int(next(tokens))
    y[i] = int(next(tokens))
    dist = math.sqrt((tx_a - x[i]) ** 2 + (ty_a - y[i]) ** 2) + \
        math.sqrt((tx_b - x[i]) ** 2 + (ty_b - y[i]) ** 2)
    if dist <= avail_range:
        print(YES)
        exit()

print(NO)
