X, Y = map(int, input().split())

l = [X]
while True:
    X *= 2
    if X > Y:
        break
    l.append(X)

print(len(l))
