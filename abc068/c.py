import sys

N, M = map(int, input().split())
abn = zip(*[map(int, sys.stdin.read().split())] * 2)

stopover = {1: {}, N: {}}
res = "IMPOSSIBLE"
for (a, b) in abn:
    if a != 1 and b != N:
        continue
    if a == 1:
        if b in stopover[N]:
            res = "POSSIBLE"
            break
        stopover[1][b] = True

    if b == N:
        if a in stopover[1]:
            res = "POSSIBLE"
            break
        stopover[N][a] = True

print(res)
