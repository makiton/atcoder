import sys
from decimal import Decimal

n = Decimal(sys.stdin.readline())

ans = []
while n > 0:
    if n % 2 == 0:
        ans.append("B")
        n /= 2
        continue
    ans.append("A")
    n -= 1

ans.reverse()
print("".join(ans))
