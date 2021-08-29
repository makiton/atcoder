from sys import stdin

s, t = map(int, stdin.readline()[:-1].split())

cnt = 0
for a in range(s+1):
    for b in range(s-a+1):
        for c in range(s-a-b+1):
            if a * b * c <= t:
                cnt += 1

print(cnt)
