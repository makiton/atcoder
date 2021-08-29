from sys import stdin
import itertools

S = [stdin.readline().rstrip().split() for _ in range(4)]
if ''.join(sorted(list(itertools.chain.from_iterable(S)))) == '2B3BHHR':
    print('Yes')
else:
    print('No')

