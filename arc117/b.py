N = int(input())
An = [0] + sorted(set(map(int, input().split())))
P = 10**9 + 7

ans = 1
for i in range(1, len(An)):
    ans *= (An[i] - An[i-1] + 1)
    ans %= P

print(ans)
