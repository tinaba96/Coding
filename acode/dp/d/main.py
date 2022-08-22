N, W = list(map(int, input().split()))

li = []

for i in range(N):
    w, v = list(map(int, input().split()))
    li.append((w, v))

dp = [[0 for i in range(W)] for j in range(N)] # i番目で重さj以下における、価値の最大値


for i in range(N-1):
    for j in range(W):
        if W > (j+li[i][0]):
            dp[i+1][j+li[i][0]] = dp[i][li[i][0]]+li[i][1]
        else:
            dp[i+1][li[i][0]] = dp[i][li[i][0]]
            

print(dp[N-1][W-1])
