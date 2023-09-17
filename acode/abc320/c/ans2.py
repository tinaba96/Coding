M = int(input())
N = 3
S = [input() for _ in range(N)]
INF = 1e9
ans = INF
for i in range(N * M):
    for j in range(N * M):
        for k in range(N * M):
            if i != j and i != k and j != k and S[0][i % M] == S[1][j % M] == S[2][k % M]:
                ans = min(ans, max(i, j, k))
print(ans if ans < INF else -1)
