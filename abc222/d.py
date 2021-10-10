N = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
M = 3000
D = 998244353

dp = [1] * (M+1)
for i in range(N):
    nx = [0] * (M+1)
    for j in range(an[i], bn[i]+1):
        nx[j] = dp[j]
    dp = nx
    for k in range(M):
        dp[k+1] += dp[k]
        dp[k+1] %= D

print(dp[-1])
