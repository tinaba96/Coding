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


N, Q = list(map(int, input().split()))

mp = [[] for i in range(N+1)]

uf = UnionFind(N+1)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        uf.union(q[1], q[2])
        mp[q[1]].append(q[2])
    elif q[0] == 2:
        # here, I need to operate UnionFind. But it is time consuming to change their parents for those dividing nodes
        ind = mp[q[1]].index(q[2])
        print(ind)
        mp[q[1]] = mp[q[1]][:ind]
        mp[q[2]]= mp[q[1]][ind:]
    else:
        i = uf.find(q[1])
        print(mp[i])

# in this case, Union Find is not the right approach
    
# union find cannot divide their groups.
# https://pyteyon.hatenablog.com/entry/2019/03/11/200000
# 「グループを繋げる」，「グループに属するか」という二つの操作が Union-Find の軸



