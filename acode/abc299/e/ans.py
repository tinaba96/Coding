from collections import deque, defaultdict

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda n : int(n) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

K = int(input())
color = [1] * N
just = defaultdict(list)
for _ in range(K):
    p, d = map(int, input().split())
    p -= 1

    Q = deque()
    Q.append(p)

    dist = [-1] * N
    dist[p] = 0

    while Q:
        i = Q.popleft()
        for j in G[i]:
            if dist[j] != -1: continue
            dist[j] = dist[i] + 1
            Q.append(j)

    for i in range(N):
        if dist[i] < d: color[i] = 0
        if dist[i] == d: just[p].append(i)

if sum(color) == 0: exit(print('No'))

for p in just.keys():
    flag = False
    for j in just[p]:
        if color[j] == 1: flag = True
    
    if not flag: exit(print('No'))

print('Yes')
print(''.join(map(str, color)))
