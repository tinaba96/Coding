'''
#A
N = 0
N = int(input())
if N%2 == 0:
    print(N//2)
else:
    print(N//2+1)
#B
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

N = int(input())
b = []
for i in range(N):
    b.append(int(input()))
bingo = False
if A[0] in b:
    if A[1] in b:
        if A[2] in b:
            bingo = True

if B[0] in b:
    if B[1] in b:
        if B[2] in b:
            bingo = True


if C[0] in b:
    if C[1] in b:
        if C[2] in b:
            bingo = True

if A[0] in b:
    if B[1] in b:
        if C[2] in b:
            bingo = True


if A[2] in b:
    if B[1] in b:
        if C[0] in b:
            bingo = True

if A[0] in b:
    if B[0] in b:
        if C[0] in b:
            bingo = True

if A[1] in b:
    if B[1] in b:
        if C[1] in b:
            bingo = True

if A[2] in b:
    if B[2] in b:
        if C[2] in b:
            bingo = True

if bingo == False:
    print('No')
else:
    print('Yes')

#C
N, M = list(map(int, input().split()))
ins = False
ans = [0]*N
ok = True
for i in range(M):
    s, c = list(map(int, input().split()))
    if N != 1 and s==1 and c==0:
        ok = False
    if ans[s-1]==0 or ans[s-1]==c:
        ans[s-1] = c
    else:
        ok = False
    if s == 1:
        ins = True
    else:
        ins = False
answer = []
if ok == True:
    for i in range(len(ans)):
        answer.append(str(ans[i]))
    #if N != 1 and ins==False:
    if N != 1 and answer[0]=='0':
        answer[0]='1'
    if N == 1 and M == 0:
        print(0)
    else:
        print(''.join(answer))
else:
    print('-1')


#D
N, M, K = list(map(int, input().split()))
#A = [[0]*N]*N
#上記の方法だと同じリストをN個用意しているだけ
A = [[0 for i in range(N)] for j in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    A[a-1][b-1] += 1
    print(A)


for i in range(K):
    c, d = list(map(int, input().split()))
    A[c-1][d-1] += 1

print(A)
'''

#Dans
class UnionFind:
    def __init__(self, n):
        self.parent = [ -1 for _ in range(n) ]
        self._size = n
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.parent[y] < self.parent[x]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self._size -= 1
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    def size(self, x):
        return -self.parent[self.root(x)]

n, m, k = map(int, input().split())
friends = [ [] for _ in range(n) ]
blocks  = [ [] for _ in range(n) ]

tree = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1;
    friends[a].append(b)
    friends[b].append(a)
    tree.unite(a, b)

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1; b -= 1;
    blocks[a].append(b)
    blocks[b].append(a)

for i in range(n):
    ret = tree.size(i)
    s = set()
    for j in friends[i]:
        s.add(j)
    for j in blocks[i]:
        if tree.same(i, j):
            s.add(j)
    ret -= len(s)
    print(ret-1)

