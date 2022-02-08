# sane approach as video edtorial using dijkstra
import sys
from heapq import heappush, heappop

sys.setrecursionlimit(1000000000)
N, M = map(int, input().split())
h = list(map(int, input().split()))
edge = [[] for _ in range(N)]
inf = float("inf")

for i in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if h[u]>h[v]:
        c = h[u]-h[v]
        edge[u].append([v, 0])
        edge[v].append([u, c])
    else:
        c = h[v]-h[u]
        edge[v].append([u, 0])
        edge[u].append([v, c])





def dijkstra(s):
    dist = [inf]*N
    dist[s] = 0
    q = []
    heappush(q, (dist[s], s))

    while(len(q)!=0):
        # print(q)
        # print(dist)
        c, v = heappop(q)
        if c > dist[v]:
            continue
        for e, cost in edge[v]:
            if dist[e] > c+cost:
                dist[e] = c+cost
                heappush(q, (c+cost, e))
    return dist

ret = dijkstra(0)

ans = 0
 
 
for i in range(N):
    ans = max(ans, -(h[i] + ret[i] - h[0]))

print(ans)
