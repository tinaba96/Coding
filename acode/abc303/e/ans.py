# dfs (video editorial)

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda n : int(n) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

root = -1
for u in range(N):
    if len(G[u]) == 1:
        root = u
        break

visited = [False] * N
ans = []
def dfs(u, dis):
    if dis % 3 == 1: ans.append(len(G[u]))

    visited[u] = True

    for v in G[u]:
        if visited[v]: continue
        visited[v] = True

        dfs(v, dis + 1)

dfs(root, 0)

ans.sort()

print(*ans)
