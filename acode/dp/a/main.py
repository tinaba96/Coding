# with a help of answer


N = int(input())
h = list(map(int, input().split()))

dp = [0 for i in range(N+1)]

for i in range(2, N+1):
    if i == 2:
        dp[i] = dp[i-1] + abs(h[i-2]-h[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(h[i-2]-h[i-1]), dp[i-2]+abs(h[i-3]-h[i-1]))

print(dp[N])




