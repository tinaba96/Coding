
import sys
sys.setrecursionlimit(500000)
n,m = map(int,input().split(' '))
edges = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split(' '))
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

visit = [False] * n

def dfs(now):
    visit[now] = True
    for e in edges[now]:
        if visit[e] == False: dfs(e)


ans = 0
for i in range(n):
    if visit[i] == True: continue
    ans += 1
    dfs(i)
print(max(0,m-n+ans))
