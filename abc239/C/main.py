#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
x = [int()] * (2)  # type: "List[int]"
y = [int()] * (2)  # type: "List[int]"
for i in range(2):
    x[i] = int(next(tokens))
    y[i] = int(next(tokens))

ps = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]
for (xd1, yd1) in ps:
    p = (x[0] + xd1, y[0] + yd1)
    for (xd2, yd2) in ps:
        if p == (x[1] + xd2, y[1] + yd2):
            print(YES)
            exit()
print(NO)
