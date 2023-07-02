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

import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N = int(input())

mp = [[] for i in range(N+1)]

uf = UnionFind(N)

for i in range(N-1):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)
    uf.union(u, v)
    

cnt = 0

for j in range(N):
    if len(mp[j]) > 2 or len(mp[j]) == 1:
        continue
    cnt += 1


print(cnt//2)

'''
考えたアプローチは、
星の中心を始点にしたBFSで連結辺を見つけ出し、
UnionFindでその辺を切っていく。 →　グラフの分離はテクニックを使えばUnionFindでもできなくはないが、重い処理だし、使う必要性がない
すると、
残った連結成分のサイズをUnionFindで求めれば、
星のレベルを求めることができる。→　星のサイズというよりは、中心の次数なので、わざわざUnionFindでサイズを求める必要はない。
'''
