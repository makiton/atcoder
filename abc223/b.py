S = input()

min_s = max_s = S
for i in range(len(S)):
    new_s = S[i:] + S[:i]
    if new_s < min_s:
        min_s = new_s
    if new_s > max_s:
        max_s = new_s

print(min_s)
print(max_s)
