from collections import defaultdict
import heapq
import sys

N, M = map(int, input().split())
P = [n for n in range(1, N+1)]

abm = sorted(
    list(zip(*[map(int, sys.stdin.read().split())] * 2)), reverse=True)

in_cnt = defaultdict(int)
outs = defaultdict(list)
for (a, b) in abm:
    in_cnt[b - 1] += 1
    outs[a-1].append(b-1)

ans = []
queue = [i for i in range(N) if in_cnt[i] == 0]
heapq.heapify(queue)

while len(queue) > 0:
    v = heapq.heappop(queue)
    ans.append(v)
    for v2 in outs[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            heapq.heappush(queue, v2)

if len(ans) != N:
    print(-1)
    exit()

print(' '.join(list(map(lambda n: str(n+1), ans))))
