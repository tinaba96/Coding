n = int(input())
a = list(map(int, input().split()))

dp = [None]*n
for i in range(n):
    dp[i] = [0, 0]
    
#行動1を行う場合→行動Nは必ずしも行う必要はない
dp[0][0] = 10**10
dp[0][1] = a[0]
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1])+a[i]
    
ans1 = min(dp[n-1][0], dp[n-1][1])

#行動1を行わない場合→行動Nは必ず行う
for i in range(n):
    dp[i] = [0, 0]
    
dp[0][0] = 0
dp[0][1] = 10**10
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1])+a[i]
    
ans2 = dp[n-1][1]


print(min(ans1, ans2))
