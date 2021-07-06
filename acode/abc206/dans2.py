N=int(input())
*A,=map(int,input().split())

#UnionFind(N)
class UnionFind:
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rank = [0]*(n+1)

  def find(self, x):
    if self.root[x] < 0:
      return x
    else:
      self.root[x] = self.find(self.root[x])
      return self.root[x]

  def unite(self, x, y):
    x, y = self.find(x), self.find(y)
    if x == y:
      return
    if self.rank[x] > self.rank[y]:
      x, y = y, x
    self.root[y] += self.root[x]
    self.root[x] = y
    self.rank[y] += self.rank[x] == self.rank[y]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def size(self, x):
    return -self.root[self.find(x)]

  def group_list(self):
    member_list = dict()
    for member in range(self.n):
      leader = self.find(member)
      if leader in member_list:
        member_list[leader].append(member)
      else:
        member_list[leader] = [member]
    return member_list
Tree=UnionFind(2*10**5)
for i in range(N):
  Tree.unite(A[i]-1,A[N-1-i]-1)
print(sum(len(v)-1for v in Tree.group_list().values()))
