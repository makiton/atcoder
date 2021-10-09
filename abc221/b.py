S = input()
T = input()

if S == T:
    print("Yes")
    exit()

for i in range(len(S) - 1):
    if T == S[:i] + S[i+1] + S[i] + S[i+2:]:
        print("Yes")
        exit()

print("No")