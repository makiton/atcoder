from sys import stdin
import itertools

p = 1000000007
CHARS = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
S = stdin.readline().rstrip().split()[0]

S = ''.join([c for c in S if c in CHARS])

ar = [list(itertools.repeat(1, len(S) + 1))] + [list(itertools.repeat(0, len(S) + 1)) for _ in range(len(CHARS))]
i = 0
for c in CHARS:
    i += 1
    j = 0
    for s in S:
        j += 1
        if c == s:
           ar[i][j] = ar[i - 1][j - 1] + ar[i][j - 1]
        else:
           ar[i][j] = ar[i][j - 1] 
print(ar[i][j] % p)
