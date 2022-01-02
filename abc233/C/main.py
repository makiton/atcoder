#!/usr/bin/env python3
N, X = map(int, input().split())
L = [0] * N
ain = [[]] * N
for i in range(N):
    a = list(map(int, input().split()))
    L[i] = a[0]
    ain[i] = a[1:]


def dfs(i, prod):
    if i >= N:
        if prod == X:
            return 1
        return 0
    cnt = 0
    for j in range(L[i]):
        if prod * ain[i][j] > X:
            continue
        cnt += dfs(i+1, prod * ain[i][j])
    return cnt


print(dfs(0, 1))
