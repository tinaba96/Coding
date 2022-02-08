from collections import defaultdict

H, W = list(map(int, input().split()))
Q = int(input())
ma = [[0 for i in range(W+2)] for j in range(H+2)]
box = set()


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

uf = UnionFind(2000*2000+1)

#print(uf)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ma[q[1]][q[2]] = 1
        if ma[q[1]-1][q[2]] == 1:
            uf.union(q[1]*(W)+q[2], (q[1]-1)*(W)+q[2])
        if ma[q[1]][q[2]-1] == 1:
            uf.union(q[1]*(W)+q[2], (q[1])*(W)+q[2]-1)
        if ma[q[1]+1][q[2]] == 1:
            uf.union(q[1]*(W)+q[2], (q[1]+1)*(W)+q[2])
        if ma[q[1]][q[2]+1] == 1:
            uf.union(q[1]*(W)+q[2], (q[1])*(W)+q[2]+1)

    else:
        if ma[q[1]][q[2]] == 1 and ma[q[3]][q[4]] == 1:
            if uf.find(q[1]*(W)+q[2]) == uf.find(q[3]*(W)+q[4]):
                print('Yes')
            else:
                print('No')
        else:
            print('No')

        



