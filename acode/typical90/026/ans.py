N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    G[x].append(y)
    G[y].append(x)
C = [-1] * N
stk = [0]
C[0] = 0
while stk:
    v = stk.pop()
    c = C[v]
    for nv in G[v]:
        if C[nv] >= 0: continue
        C[nv] = c ^ 1
        stk.append(nv)
c = 1 if C.count(1) >= N // 2 else 0
c = 1 if C.count(1) >= N // 2 else 0
print(*[i + 1 for i in range(N) if C[i] == c][:N // 2])



