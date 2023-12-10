N = int(input())

G = [[] for i in range(N)]
used = [False] * N
times = [0] * N

for i in range(N):
    t, k, *A = map(int, input().split())
    for a in A:
        G[i].append(a-1)
    times[i] = t


used[N-1] = True

ans = 0

for i in reversed(range(N)):
    if used[i]:
        ans += times[i]
        for g in G[i]:
            used[g] = True

print(ans)
