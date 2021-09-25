S = input()

for i in range(len(S)-1):
    for j in range(i, len(S)):
        if S[:i] + S[j:] == 'keyence':
            print("YES")
            exit()

print("NO")
