import sys

N = int(sys.stdin.readline())
pn = map(int, sys.stdin.readline().split())
res = [0] * N
for i, p in enumerate(pn):
    res[p-1] = i + 1

print(' '.join(map(str, res)))
