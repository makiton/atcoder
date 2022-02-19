#!/usr/bin/env python3
import sys
from collections import deque


class Node:
    def __init__(self, id, num):
        self.id = id
        self.num = num
        self.links = []
        self._numbers = None
        if id == 0:
            self.uplink = self
        else:
            self.uplink = None

    def link(self, node):
        if node.id == 0:
            self.uplink = node
            for node in self.links:
                node.set_uplink(self)
        self.links.append(node)

    def set_uplink(self, node):
        if self.uplink is not None:
            return
        self.uplink = node
        for node in self.links:
            node.set_uplink(self)

    def find_uplink(self, exclude_node=None):
        if self.uplink is not None:
            return self.uplink
        for node in self.links:
            if node == exclude_node:
                continue
            if node.find_uplink(self) is not None:
                self.uplink = node
                return node
        return None

    def numbers(self):
        if self._numbers is not None:
            return self._numbers

        uplink = self.find_uplink()
        ret = [self.num]
        for node in self.links:
            if node == uplink:
                continue
            ret += node.numbers()
        self._numbers = ret
        return ret


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word


tokens = iterate_tokens()
N = int(next(tokens))  # type: int
Q = int(next(tokens))  # type: int
nodes = [Node(i, int(next(tokens))) for i in range(N)]  # type: "List[int]"
for i in range(N - 1):
    a = int(next(tokens)) - 1
    b = int(next(tokens)) - 1
    nodes[a].link(nodes[b])
    nodes[b].link(nodes[a])

for i in range(Q):
    v = int(next(tokens)) - 1
    k = int(next(tokens))
    print(sorted(nodes[v].numbers(), reverse=True)[k-1])
