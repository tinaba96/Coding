# these are not linear approach but there is also an approach of linear explained in video editorial

import sys
from collections import deque


def getnum():
    return int(sys.stdin.readline())


def getlist():
    return list(map(int, sys.stdin.readline().split()))


n, m = getlist()
INF = float('inf')
g = [[] for _ in range(n + 1)]
dis = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = getlist()
    g[a].append(b)
    g[b].append(a)

# for i in range(1, n + 1):
#     dis[i][i] = 0

for i in range(1, n + 1):
    dis[i][i] = 0
    que = deque([i])
    while que:
        t = que[0]
        que.popleft()
        for ne in g[t]:
            if dis[i][ne] != -1:
                continue
            dis[i][ne] = dis[i][t] + 1
            que.append(ne)

# for _ in dis:
#     print(*_)

st = [True] * (n + 1)
k = getnum()
# print(k)
pq = [getlist() for _ in range(k)]
for p, q in pq:
    # p, q = getlist()
    for i in range(1, n + 1):
        if dis[p][i] < q:
            st[i] = False
# print()

valid = True
for p, q in pq:
    find = False
    for i in range(1, n + 1):
        if dis[p][i] == q and st[i]:
            find = True
            break
    if not find:
        valid = False
        break

if st.count(False) == n or not valid:
    print('No')
else:
    print('Yes')
    for i in range(1, n + 1):
        print('1' if st[i] else '0', end='')
    print()


'''
import heapq
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n,m = readints()

path = [[] for i in range(n)]

for i in range(m):
    u,v = readints()
    path[u-1].append(v-1)
    path[v-1].append(u-1)

k = readint()
pd = []
for i in range(k):
    p,d = readints()
    pd.append([p-1,d])

distmap = [[10**10 for i in range(n)] for j in range(n)]
for start in range(n):
    h = [(0,start)]
    distmap[start][start] = 0
    while h:
        l,p = heapq.heappop(h)
        for x in path[p]:
            if distmap[start][x]>l+1:
                distmap[start][x] = l+1
                heapq.heappush(h,(l+1,x))

s = [1 for i in range(n)]
for p,d in pd:
    for i in range(n):
        if distmap[p][i]<d:
            s[i] = 0

flag = 1
for p,d in pd:
    flag = 0
    for i in range(n):
        if distmap[p][i]==d and s[i]==1:
            flag += 1
    if not flag:
        break

if flag:
    print('Yes')
    print(''.join(map(str,s)))
else:
    print('No')

'''

