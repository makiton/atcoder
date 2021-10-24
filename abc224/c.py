import sys
N = int(input())
xyn = list(zip(*[map(int, sys.stdin.read().split())] * 2))

cnt = 0
for i1 in range(N-2):
    x1, y1 = xyn[i1]
    for i2 in range(i1+1, N-1):
        x2, y2 = xyn[i2]
        for i3 in range(i2+1, N):
            x3, y3 = xyn[i3]
            if (x3-x1)*(y2-y1) == (y3-y1)*(x2-x1):
                continue
            cnt += 1
print(cnt)
