from sys import stdin
import itertools


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.s = [1] * n

    def unite(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.s[u] < self.s[v]:
            u, v = v, u
        self.s[u] += self.s[v]
        self.p[v] = u

    def find(self, u):
        if self.p[u] == u:
            return u
        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def size(self, u):
        return self.s[self.find(u)]

n = int(stdin.readline()[:-1])
uvw = map(int, stdin.read().split())
uvw = sorted(list(zip(*[uvw] * 3)), key = lambda n: n[2])

ans = 0
uf = UnionFind(n)

for u, v, w in uvw:
    u -= 1
    v -= 1
    ans += uf.size(u) * uf.size(v) * w
    uf.unite(u, v)

print(ans)
