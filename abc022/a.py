import sys

N, S, T = map(int, sys.stdin.readline().split())
W = int(sys.stdin.readline())

cnt = 1 if W >= S and W <= T else 0
for i in range(1, N):
    Ai = int(sys.stdin.readline())
    W += Ai
    if W >= S and W <= T:
        cnt += 1

print(cnt)
