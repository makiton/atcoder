import math
import itertools
import copy

N = sorted(list(input()), reverse=True)

m = 0
for i in range(1, math.ceil(len(N)/2)+1):
    for a in set(itertools.combinations(N, i)):
        digits = copy.copy(N)
        for d in a:
            digits.remove(d)
        mul = int(''.join(a)) * int(''.join(digits))
        if m < mul:
            m = mul

print(m)