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


N, M = list(map(int, input().split()))

num = [0 for n in range(N+1)]

uf = UnionFind(N+1)

for i in range(M):
    u, v = list(map(int, input().split()))
    uf.union(u, v)
    num[u] += 1
    num[v] += 1

tot_num = uf.group_count()-1

seen = [False for g in range(N+1)]

#for a in range(tot_num):

#print(tot_num)

#print(uf)
#print(uf.all_group_members().items())

#print(uf.all_group_members().values())

#print(num)

ans = True

for w in uf.all_group_members().values():
#for w in uf.all_group_members().values():
    #print(w)
    y = 0
    l = len(w)
    for b in range(l):
        y += num[b+1]
        #print(w[b])
    y /= 2

    #print('y: ', int(y))
    #print('l: ', l)

    if int(y) != l:
        ans = False
    
    #print('-')

print(ans)



