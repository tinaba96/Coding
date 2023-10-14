def minimum_voters_to_win(N, data):
    INF = 1e18
    X, Y, Z = zip(*data)  # dataからX, Y, Zのリストを取得

    z_sum = sum(Z)

    # dp[j]はj議席を獲得するために必要な最小の鞍替え人数
    dp = [INF] * (z_sum + 1)
    dp[0] = 0
    
    for i in range(N):
        x, y, z = X[i], Y[i], Z[i]
        w = max(0, (x + y) // 2 + 1 - x)
        for j in range(z_sum, z - 1, -1):
            dp[j] = min(dp[j], dp[j - z] + w)

    return min(dp[z_sum // 2 + 1:])


N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]


print(minimum_voters_to_win(N, data))

# smart way in terms of space complexity -> video editorial

