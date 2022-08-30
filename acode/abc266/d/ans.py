N = int(input())
snuke = [ [] for i in range(10**5 + 1) ]
for i in range(N):
    T, X, A = map(int, input().split())
    snuke[T] = [X, A]

INF = float('inf')
dp = [ [-INF] * (10**5 + 1) for i in range((5+1)) ]
dp[0][0] = 0

for j in range(1, 10**5 + 1):
    for i in range(4+1):
        if snuke[j] == [] or (not snuke[j][0] == i):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1])
            elif i == 5:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])
            continue

        value = snuke[j][1]
        if i == 0:
            dp[i][j] = max(dp[i][j-1] + value, dp[i+1][j-1] + value)
        elif i == 5:
            dp[i][j] = max(dp[i][j-1] + value, dp[i-1][j-1] + value)
        else:
            dp[i][j] = max(dp[i][j-1] + value, dp[i+1][j-1] + value, dp[i-1][j-1] + value)

ans = 0
for i in range(4 + 1):
    ans = max(ans, dp[i][-1])

print(ans)
