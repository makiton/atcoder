import sys
ss = sys.stdin.readline()

ans = 0
print(len(ss))
for s in list(ss):
    if s == "A":
        ans += 1
    if s == "B":
        ans *= 2

print(ans)
