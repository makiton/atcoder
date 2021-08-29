from sys import stdin

n = int(stdin.readline()[:-1])
if n <= 125:
    print(4)
elif n <= 211:
    print(6)
else:
    print(8)
