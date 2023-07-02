# maybe easier implementation


N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

count = [0] * N
for i in range(N):
    count[len(g[i])] += 1

ans = []
v_sum = 0
for i in range(N): # from smaller to bigger one
    if i >= 3:
        v_sum += ((i + 1) * count[i])
        ans += [i] * count[i]

two = [2] * ((N - v_sum) // 3)  # size two
ans = two + ans
print(*ans)
