import sys

N = int(input())
abn = list(zip(*[map(int, sys.stdin.read().split())] * 2))

t = 0
for (a, b) in abn:
    t += a / b

t /= 2

left_t = 0
left_a = 0
for (a, b) in abn:
    td = a / b
    if t <= left_t + td:
        left_a += (t - left_t) * b
        break

    left_a += a
    left_t += td

print(left_a)
