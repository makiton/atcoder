N, P = map(int, input().split())
cnt = 0
for a in map(int, input().split()):
    if a < P:
        cnt+=1

print(cnt)