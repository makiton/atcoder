from collections import deque

N = 9
M = int(input())

uvm = []
to = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda n: int(n)-1, input().split())
    to[u].append(v)
    to[v].append(u)


pi = [-1] * N
for i, n in enumerate(map(lambda n: int(n)-1, input().split())):
    pi[n] = i

ti = [n for n in range(N-1)] + [-1]

k = ''.join(map(str, pi))
dist = {k: 0}
q = deque([pi])
while len(q) > 0:
    s = q.popleft()
    k = ''.join(map(str, s))
    d = dist[k]
    for i in range(N):
        if s[i] == -1:
            for t in to[i]:
                s2 = s[:]
                s2[i], s2[t] = s2[t], -1
                k = ''.join(map(str, s2))
                if k not in dist:
                    dist[k] = d+1
                    q.append(s2)
            break

k = ''.join(map(str, ti))
if k in dist:
    print(dist[k])
else:
    print(-1)
