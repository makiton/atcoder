import sys
import itertools

N = int(input())
tn = list(map(int, sys.stdin.read().split()))
total = sum(tn)
min_t = total

for i in range(1, N):
    for sub in itertools.combinations(tn, i):
        sub_t = sum(sub)
        min_t = min(min_t, max(sub_t, total-sub_t))

print(min_t)
