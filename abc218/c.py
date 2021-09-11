import sys
import numpy as np

N = int(sys.stdin.readline())

S = []
cntS = 0
for i in range(N):
    tmp = list(sys.stdin.readline()[:-1])
    cntS += tmp.count('#')
    S.append(tmp)

T = []
cntT = 0
for i in range(N):
    tmp = list(sys.stdin.readline()[:-1])
    cntT += tmp.count('#')
    T.append(tmp)

if cntS != cntT:
    print("No")
    exit()


def trim(s):
    res = []
    m = N
    inShape = False
    for row in s:
        try:
            idx = row.index('#')
            inShape = True
        except ValueError:
            if inShape:
                res.append(row)
            continue
        if m > idx:
            m = idx
        res.append(row)

    if m >= N:
        return res
    return [row[m:] for row in res]


def rotate(s):
    return np.array(s)[::-1, :].T.tolist()


def match(s, t):
    for i, row in enumerate(s):
        if i >= len(t):
            if '#' in row:
                return False
            continue
        for j, c in enumerate(row):
            if j >= len(t[i]):
                if c == '#':
                    return False
                continue
            if t[i][j] != c:
                return False
    return True


S = trim(S)
T = trim(T)
if match(S, T):
    print("Yes")
    exit()
for _ in range(3):
    T = trim(rotate(T))
    if match(S, T):
        print("Yes")
        exit()

print("No")
