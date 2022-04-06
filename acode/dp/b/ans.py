N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

# print(N, K, h)

# 足場 1 から i への移動に必要な最低コストをdp[i]とおく
dp = [0] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    costs = []
    for j in range(K):
        if j + 1 > i:
            continue
        costs.append(dp[i - j - 1] + abs(h[i] - h[i - j - 1]))
    dp[i] = min(costs)

print(dp[-1])
