import sys
H, W = map(int, input().split())
aij = list(map(list, sys.stdin.read().split()))

rowflg = [True] * H
colflg = [True] * W
for i in range(H):
    for j in range(W):
        rowflg[i] &= aij[i][j] != '#'
        colflg[j] &= aij[i][j] != '#'

for i in range(H):
    if rowflg[i]:
        continue
    print(''.join([a for j, a in enumerate(aij[i]) if not colflg[j]]))
