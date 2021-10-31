import sys
N = int(input())
abn = list(zip(*[map(int, sys.stdin.read().split())] * 2))

nodes = set(abn[0])
for i in range(N-1):
    nodes &= set(abn[i])

if len(nodes) > 0:
    print("Yes")
else:
    print("No")
