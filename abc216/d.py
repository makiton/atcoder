import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

t = []
q = deque()
mem = [[] for _ in range(n)]
for i in range(m):
    k = int(sys.stdin.readline())
    qq = deque(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
    t.append(qq)
    mem[qq[0]].append(i)
    if len(mem[qq[0]]) == 2:
        q.append(qq[0])

c = 0
while q:
    nn = q.popleft()
    c += 1
    for i in mem[nn]:
        qq = t[i]
        qq.popleft()
        if qq:
            mem[qq[0]].append(i)
            if len(mem[qq[0]]) == 2:
                q.append(qq[0])

if c == n:
    print("Yes")
else:
    print("No")
