#!/usr/bin/env python3
import sys


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
W = [next(tokens) for _ in range(N)]  # type: "List[str]"

last_char = W[0][0]
turn = 0
words = set()
for w in W:
    if w[0] != last_char or w in words:
        if turn == 0:
            print('LOSE')
            exit()
        else:
            print('WIN')
            exit()
    words.add(w)
    last_char = w[-1]
    turn ^= 1

print('DRAW')
