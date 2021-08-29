from sys import stdin
import itertools

n = int(stdin.readline()[:-1])
s = list(map(int, stdin.readline()[:-1].split()))
t = list(map(int, stdin.readline()[:-1].split()))


min_t = 1000000001
min_i = 0
for i, t_i in enumerate(t):
    if min_t > t_i:
        min_t = t_i
        min_i = i

ans = list(itertools.repeat(0, n))
ans[min_i] = min_t

i = min_i
while True:
    acm = ans[i] + s[i]
    i += 1
    if i >= n:
        i = 0
    if min_i == i:
        break

    ans[i] = min(t[i], acm)


for a in ans:
    print(a)
