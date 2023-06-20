from heapq import heapify, heappop, heappush

n, m, k = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [-1] * n
que = []
heapify(que)

for _ in range(k):
    u, d = map(int, input().split())
    u -= 1
    seen[u] = d
    que.append((-d, u))
while que:
    d, u = heappop(que)
    d = -d
    for v in G[u]:
        if seen[v] >= d - 1: continue
        seen[v] = d - 1
        heappush(que, (-d+1, v))

ret = []
for i in range(n):
    if seen[i] == -1: continue
    ret.append(i+1)

print(len(ret))
print(*ret)
