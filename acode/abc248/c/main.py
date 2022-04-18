import math

N, M, K = list(map(int, input().split()))

mod = 998244353

m = K//N

#print(m)
#print(m**M%mod)

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

#print(permutations_count(m, M))

dp = [[0 for i in range(N+1)] for j in range(M+1)]

for i in range(M+1):
    dp[i][0] = 1

for i in range(1, N):
    for j in range(1, M):
        for k in range(1, M):
            dp[j][i] += dp[k][i-1]


#print(sum(dp[N])%mod)


print(((20**31)-(19**31))%mod)
