import sys

N, M = map(int, input().split())
B = list(zip(*[map(int, sys.stdin.read().split())] * M))

origin = B[0][0]
i_max = 10 ** 100

for j in range(1, 8):
    if (origin - j) % 7 != 0:
        continue
    i = int((origin - j) / 7 + 1)
    if i <= 0 or i > i_max:
        continue
    match = True
    for id in range(N):
        if i + id > i_max:
            match = False
            break
        for jd in range(M):
            if j+jd > 7:
                match = False
                break
            match &= (B[id][jd] == (i+id-1)*7+j+jd)

    if match:
        print("Yes")
        exit()

print("No")
