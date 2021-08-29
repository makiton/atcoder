import sys

n, m = map(int, sys.stdin.readline().split())

deps = [[] for _ in range(n)]
for _ in range(m):
    k = int(sys.stdin.readline())
    aij = list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
    for j in range(k):
        for jj in range(j + 1, k):
            deps[aij[jj]].append(aij[j])
            if aij[jj] in deps[aij[j]]:
                print("No")
                exit()
print("Yes")
