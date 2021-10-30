from collections import deque

S = {
    'a': deque(input()),
    'b': deque(input()),
    'c': deque(input())
}

c = S['a'].popleft()
while True:
    if len(S[c]) == 0:
        print(c.upper())
        break
    c = S[c].popleft()
