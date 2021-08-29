import sys

x, y = map(int, sys.stdin.readline().split("."))
if y <= 2:
    print(f"{x}-")
elif y <= 6:
    print(x)
else:
    print(f"{x}+")
