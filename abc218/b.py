import sys

Pi = map(lambda p: chr(int(p) - 1 + ord('a')), sys.stdin.readline().split())

print(''.join(Pi))
