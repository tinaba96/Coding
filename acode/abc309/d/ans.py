from collections import defaultdict #default_dict = defaultdict(関数名)
import sys
from itertools import product #bit全探索 for pro in product((0, 1), repeat=N):
from collections import deque

# 入力受取り
N1, N2, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    # BFS準備
    dist = [-1] * (N1+N2+1)
    dist[start] = 0
    #dist[1] = 0
    d = deque()
    d.append(start)

    # それぞれの経路への最短経路を計算
    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
    
    # 頂点startから、それぞれの頂点への最短経路の中で、最大値を返す
    ans = dist[1:]
    return max(ans)

max_route_from_one = bfs(1)
max_route_from_last = bfs(N1+N2)

# それぞれのグループの、頂点1 or N1+N2 からの最短経路の最大値に1を足すと答え
ans = max_route_from_one + max_route_from_last + 1
print(ans)

