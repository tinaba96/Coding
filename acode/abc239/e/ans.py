import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
X = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    graph[A].append(B)
    graph[B].append(A)

def merge(a, b, k=20):
    a.extend(b)
    a.sort(reverse=True)
    a = a[:k]
    return a

s = [[X[i]] for i in range(N)]
def dfs(v, prev=-1):
    for u in graph[v]:
        if u == prev: 
            continue
        s[v] = merge(s[v], dfs(u, v))
    return s[v]

dfs(0)
for i in range(Q):
    V, K = map(int, input().split())
    V, K = V - 1, K - 1
    print(s[V][K])


