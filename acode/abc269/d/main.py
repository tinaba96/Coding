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

N = int(input())
uf = UnionFind(N)

black = set()
ans = 0

loop = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
 

for i in range(N):
    A = list(map(int, input().split()))
    black.add(str(A))
    cnt = 0
    cc = 0

    for p in loop:
        #print(p[0], p[1])
        f = True
        if str([A[0]+p[0], A[0]+p[1]]) in black:
            f = False
            cnt += 1
        else:
            if f == False:
                cc += 1
            f = True

            #print('f')
    cnt = cc
    if cnt == 0:
        ans += 0
    elif cnt == 1:
        ans += 1
    else:
        ans += 1-cnt
        


#print(black)
print(ans)

    

