import sys

n = int(sys.stdin.readline())
st = list(zip(*[sys.stdin.readlines()]*2))

for i in range(n):
    for j in range(i+1, n):
        if st[i] == st[j]:
            print("Yes")
            exit()
print("No")
