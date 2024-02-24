N = int(input())

mp = [[0 for i in range(5)] for j in range(10**5+1)]


for i in range(N):
    T, X, A = list(map(int, input().split()))
    mp[T][X] = A


# dp[t][x] t 秒後の位置xの最大値

dp = [[0 for i in range(5)] for j in range(10**5+1)]

for t in range(1, 10**5):
    for x in range(5):
        if x == 0:
            #print(t, x)
            dp[t][x] = max(dp[t][x], dp[t-1][x]+mp[t][x])
        else:
            dp[t][x] = max(dp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x-1]+mp[t][x])

#print(dp)
ans = 0
for a in range(5):
    ans = max(ans, dp[-2][a])

print(ans)




