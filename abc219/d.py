import sys

N = int(input())
X, Y = map(int, input().split())

abn = list(zip(*[map(int, sys.stdin.read().split())]*2))

INF = float("Inf")
dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i, (a, b) in enumerate(abn):
    for x in range(X+1):
        for y in range(Y+1):
            dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])
            dp[i+1][min(X, x+a)][min(Y, y+b)] = min(dp[i+1]
                                                    [min(X, x+a)][min(Y, y+b)], dp[i][x][y] + 1)

if dp[-1][-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1][-1])
