import sys

H, W = map(int, input().split())
aij = list(zip(*[map(int, sys.stdin.read().split())] * W))

for i1 in range(H-1):
    for j1 in range(W-1):
        for i2 in range(i1+1, H):
            for j2 in range(j1+1, W):
                if aij[i1][j1] + aij[i2][j2] > aij[i2][j1] + aij[i1][j2]:
                    print("No")
                    exit()
print("Yes")
