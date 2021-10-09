import sys

N = int(input())
abn = list(zip(*[map(int, sys.stdin.read().split())] * 2))

ranges = [[]] * N

xs = []
for a, b in abn:
    xs.append((a, 1))
    xs.append((a+b, -1))

ans = [0] * (N+1)
cnt = 0
xs = sorted(xs)
for i in range(1, len(xs)):
    cnt += xs[i-1][1]
    ans[cnt] += xs[i][0] - xs[i-1][0]

print(' '.join(map(str, ans[1:])))