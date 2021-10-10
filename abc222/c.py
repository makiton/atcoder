import sys

N, M = map(int, input().split())
aij = list(map(list, sys.stdin.read().split()))
aij.reverse()
won = [(0, 2*N-i-1) for i in range(N * 2)]

for j in range(M):
    for k in range(N):
        p1 = k*2
        p2 = k*2+1
        w1, i1 = won[p1]
        w2, i2 = won[p2]
        if aij[i1][j] == aij[i2][j]:
            continue
        if aij[i1][j] == 'G' and aij[i2][j] == 'C':
            won[p1] = (w1+1, i1)
        elif aij[i1][j] == 'G' and aij[i2][j] == 'P':
            won[p2] = (w2+1, i2)
        elif aij[i1][j] == 'C' and aij[i2][j] == 'P':
            won[p1] = (w1+1, i1)
        elif aij[i1][j] == 'C' and aij[i2][j] == 'G':
            won[p2] = (w2+1, i2)
        elif aij[i1][j] == 'P' and aij[i2][j] == 'G':
            won[p1] = (w1+1, i1)
        elif aij[i1][j] == 'P' and aij[i2][j] == 'C':
            won[p2] = (w2+1, i2)

    won = sorted(won, reverse=True)

for _, i in sorted(won, reverse=True):
    print(N*2-i)