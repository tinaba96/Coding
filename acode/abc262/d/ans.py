n=int(input())
a = list(map(int, input().split()))

ans=0
for i in range(1, n + 1):#
    dp = [[[0] * i for _ in range(i + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for j in range(n):
        for k in range(i + 1):
            for l in range(i):
                dp[j + 1][k][l] += dp[j][k][l]
                dp[j + 1][k][l] %= 998244353
                if k != i:
                    dp[j + 1][k + 1][(l+a[j]) % i] += dp[j][k][l]
                    dp[j + 1][k + 1][(l+a[j]) % i] %= 998244353
    ans += dp[n][i][0]
    ans %= 998244353
print(ans)

