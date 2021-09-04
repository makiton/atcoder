import sys
import bisect
import array

L, Q = map(int, sys.stdin.readline().split())

cxn = list(zip(*[map(int, sys.stdin.read().split())] * 2))
a = array.array('i', [0, L])
for c, x in cxn:
    if c == 1:
        bisect.insort_left(a, x)
    else:
        i = bisect.bisect_left(a, x)
        print(a[i] - a[i-1])
