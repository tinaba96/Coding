# --------------------------------------------
# UnionFindクラスの定義
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 変数 parents 
    # 各要素の親要素の番号、要素が根（ルート）の場合は(-1)*そのグループの要素数

    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # # 親要素は要素番号の小さい方
        # if self.parents[x] > self.parents[y]:
        # 親要素は要素番号の大きい方
        if x < y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
# --------------------------------------------


N=2**20
# N=5
# print(N,N*2)
Q = int(input())
A = [-1]*N

next = range(N)

# UfTree作成
UfTree = UnionFind(N)

for _ in range(Q):
    t,x = map(int,input().split())
    
    if t == 1:
        h = x - 1
        HmodN = h % N

        Z = UfTree.find(HmodN)
        if Z < N-1:
            A[Z] = x
            UfTree.union(Z,Z+1)
        if Z == N-1 :
            if A[Z] == -1:
                A[Z] = x
            else:
                Z = UfTree.find(0)
                A[Z] = x
                UfTree.union(Z,Z+1)

    else: # t == 2
        x=x-1
        print(A[x % N])


