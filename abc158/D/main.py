#!/usr/bin/env python3
import sys

S = input()
Q = int(input())

reverse = False
front = ''
back = ''
for line in sys.stdin.readlines():
    Qi = line.split()
    if Qi[0] == '1':
        reverse ^= True
        continue
    else:
        if (Qi[1] == '1' and not reverse) or (Qi[1] == '2' and reverse):
            front += Qi[2]
        else:
            back += Qi[2]

if reverse:
    print(''.join(list(reversed(back)))+''.join(list(reversed(S)))+front)
else:
    print(''.join(list(reversed(front)))+S+back)
