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
    d = -d # use negative for heapq
    if seen[u] != d: # this is not necessary since the number of pair that is going to be pushed to heapq will be same (maximum 2M times)
        continue # if we did not implement this, it will still AC -> each v in heapq (max 2M Vs) will have loop for the connected node which will not update the val in "seen" -> worst case O(2M*M) or O(2M*max(connected node))
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


# FYI
# https://www.youtube.com/watch?v=_tRLPjky9SQ
