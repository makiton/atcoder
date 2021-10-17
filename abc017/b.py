import re

S = input()

regex = re.compile('^(ch|o|k|u)*$')
if regex.match(S):
    print("YES")
else:
    print("NO")
