#!/usr/bin/env python3
import sys
import math


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
H = int(next(tokens))  # type: int

print(math.sqrt((H*(12800000+H))))
