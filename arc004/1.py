import sys
import math

n = int(sys.stdin.readline())
xy = list(zip(*[map(int, sys.stdin.read().split())] * 2))

max_l = 0
for i in range(len(xy)):
    for j in range(i+1, len(xy)):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        l = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if l > max_l:
            max_l = l
print(max_l)
