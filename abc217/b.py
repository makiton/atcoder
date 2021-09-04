import sys

CONTESTS = set(['ABC', 'ARC', 'AGC', 'AHC'])
inputs = sys.stdin.read().split()

print(list(CONTESTS - set(inputs))[0])
