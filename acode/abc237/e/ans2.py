from heapq import heappush, heappop

INF = -1 * 10 ** 15

N, M = map(int, input().split())
H = list(map(int, input().split()))
roots = [[] for _ in range(N + 1)]
enjoy = [INF for _ in range(N + 1)]
seen = [False for _ in range(N + 1)]
for _ in range(M):
    U, V = map(int, input().split())
    roots[U].append(V)
    roots[V].append(U)

enjoy[1] = 0
hq = [(0, 1)]
while hq:
    dist, v = heappop(hq)
    if seen[v] == True:
        continue
    seen[v] = True
    for to in roots[v]:
        if H[v - 1] - H[to - 1] > 0:
            cost = H[v - 1] - H[to - 1]
        else:
            cost = 2 * (H[v - 1] - H[to - 1])
        if seen[to] == False:
            enjoy[to] = max(enjoy[v] + cost, enjoy[to])
            heappush(hq, (dist + abs(H[to - 1] - H[v - 1]), to))

print(max(enjoy))



