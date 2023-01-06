N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)

# dp[i][j] = i番目まで見たとき、価値jのときの重さの最小値
dp = [[float("inf")] * (10**5+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10**5+1):
        if j-v[i] >= 0:
            # 取るとき
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-v[i]] + w[i])
        # 取らないとき
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

for i in range(10**5+1):
    if dp[N][10**5-i] <= W:
        print(10**5-i)
        break



'''
n,W = list(map(int, input().split()))
w = []
v = []
for _ in range(n):
    a,b = list(map(int, input().split()))
    w.append(a)
    v.append(b)
sum_v = sum(v)
dp =[[W+1]*(sum_v+1) for _ in range(n)]
# i = 0
# for i in range(sum_v+1):
dp[0][0]=0
dp[0][v[0]]=w[0]
# print(f'{dp[0][v[0]]a=}')
for i in range(1,n):
    for j in range(sum_v+1):
        dp[i][j] = min(dp[i][j],dp[i-1][j])
        if 0<=j-v[i]:
            # print(f'{ min(dp[i][j],dp[i-1][j-v[i]]+w[i])=}')
            dp[i][j] = min(dp[i][j],dp[i-1][j-v[i]]+w[i])
        # print('----')
# [print(i[0],i) for i in enumerate(dp)]
for i in range(sum_v+1):
    if dp[-1][i]<=W:
        ans = i
print(ans)
'''
