import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, K, D = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [[0 for w in range(N+1)] for h in range(N+1)]

dp[0][0] = 0
for z in range(N):
    dp[z][0] = a[z]

for i in range(K+1):
    for j in range(N):
        for k in range(N):
            if i+1 <= K and k != j:
                dp[k][i+1] = max(dp[k][i+1], dp[j][i] + a[k])
            dp[k][i] = max(dp[k][i], dp[j][i])  # this shoulf be checked

print(dp)

ans = -1
for v in range(N):
    print(dp[v][K])
    if dp[v][K] % D == 0:
        ans = max(ans, dp[v][K])

print(ans)
