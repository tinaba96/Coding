N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# dp[i][m] iまで決めた上で、選んだ数mの時の最大ち

INF = 100100100100

dp = [[-INF for i in range(M+1)] for j in range(N+1)]

dp[0][0] = 0

for x in range(N):
    for t in range(M+1):
        if (t != M):
            dp[x+1][t+1] = max(dp[x+1][t+1], dp[x][t]+((t+1)*A[x]))
        dp[x+1][t] = max(dp[x+1][t], dp[x][t])

#for i in range(N+1):
#    print(dp[i])

ans = 0
for a in range(N+1):
    ans = max(ans, dp[a][M])

print(dp[N][M])


