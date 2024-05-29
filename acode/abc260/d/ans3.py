import sys,bisect,collections,copy,heapq,itertools,math
# import numpy as np
from decimal import Decimal, ROUND_HALF_UP
from functools import lru_cache
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LIN(N): return [I() for _ in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LSN(N): return [S() for _ in range(N)]
sys.setrecursionlimit(10**6)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')


from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
    N, K = LI()
    P = LI()

    uft = UnionFind(N+1)
    tops = []
    ans = [-1] * (N + 1)

    for i, p in enumerate(P):
        idx = bisect.bisect_left(tops, p)
        if idx < len(tops):
            uft.union(tops[idx], p)
            tops[idx] = p
        else:
            # bisect.insort(tops, p)
            tops.append(p)
        if uft.size(p) >= K:
            ans[uft.find(p)] = i + 1
            del tops[idx]
            # deleted = False
            # for m in uft.members(p):
            #     ans[m] = i + 1
            #     if not deleted and m in tops:
            #         tops.remove(m)
            #         deleted = True

    for x in range(1, N+1):
        print(ans[uft.find(x)])
    # print(*ans[1:], sep="\n")


if __name__ == '__main__':
    main()

# comment on the video tutorial
#カードを重ねる時にUnionFindでくっつけて、食べる瞬間の先頭カードにだけターン情報を記録するようにしてました
