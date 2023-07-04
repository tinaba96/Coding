# have not understand this yet
import sys

sys.setrecursionlimit(220000)
N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
point = [-1] * (N + 1)
gr = []

for i in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

comp = {*range(1, N + 1)}

def BFS(i, n):
    global point, comp, gr
    for j in edges[i]:
        if j in comp:
            point[j] = 2 * n + 1 - point[i]
            gr[point[j]] += 1
            comp.remove(j)
            BFS(j, n)
        else:
            if point[j] != 2 * n + 1 - point[i]:
                exit(print(0))

now = 0
while len(comp) > 0:
    gr.append(0)
    gr.append(0)
    temp = comp.pop()
    gr[now] += 1
    point[temp] = now
    BFS(temp, now)
    now += 2

ans = 0
for i in gr:
    ans += i * (N - i)
print(ans // 2 - M)
