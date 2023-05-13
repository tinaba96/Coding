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


