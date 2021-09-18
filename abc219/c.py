import sys

X = {c: i for i, c in enumerate(list(input()))}
N = int(input())
SN = sys.stdin.read().split()


class NewDict:
    def __init__(self, obj, *args):
        self.obj = obj

    def __lt__(self, other):
        return self.mycmp(self.obj, other.obj) < 0

    def __gt__(self, other):
        return self.mycmp(self.obj, other.obj) > 0

    def __eq__(self, other):
        return self.mycmp(self.obj, other.obj) == 0

    def __le__(self, other):
        return self.mycmp(self.obj, other.obj) <= 0

    def __ge__(self, other):
        return self.mycmp(self.obj, other.obj) >= 0

    def __ne__(self, other):
        return self.mycmp(self.obj, other.obj) != 0

    def mycmp(self, a, b):
        for i, c1 in enumerate(a):
            if len(b) <= i:
                return 1
            if X[c1] > X[b[i]]:
                return 1
            if X[c1] < X[b[i]]:
                return -1
        if len(a) < len(b):
            return -1
        return 0


for s in sorted(SN, key=NewDict):
    print(s)
