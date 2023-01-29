class UnionFind():
    def __init__(self, n):
        self._n = n
        self._roots = [-1] * (n + 1)
        self._ranks = [0] * (n + 1)
    def root(self, x):
        if self._roots[x] < 0:
            return x
        self._roots[x] = self.root(self._roots[x])
        return self._roots[x]
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self._ranks[x] < self._ranks[y]:
            self._roots[y] += self._roots[x]
            self._roots[x] = y
        else:
            self._roots[x] += self._roots[y]
            self._roots[y] = x
            if self._ranks[x] == self._ranks[y]:
                self._ranks[x] += 1
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def size(self, x):
        return - self._roots[self.root(x)]
    def count_groups(self):
        return len([i for i, v in enumerate(self._roots[1:]) if v < 0])

flag = True

N, M = map(int, input().split())
if M != N - 1:
    print("No")
    exit()

check = UnionFind(N)
edges = [0] * N
for _ in range(M):
    edge_1, edge_2 = map(int, input().split())
    check.unite(edge_1, edge_2)
    edges[edge_1-1] += 1
    edges[edge_2-1] += 1
if check.count_groups() != 1:
    flag = False

#print(edges)
for v in edges:
    #print(v)
    if v > 2:
        flag = False

if flag:
    print("Yes")
else:
    print("No")

# M=N-1かつ連結かつどの頂点も次数が2以下」が必要十分条件なのだ！　3つの条件のうちどれか1つが足りないときにどんな反例があるか考えてみるのだ
# https://twitter.com/kyopro_friends/status/1619331431687397378
