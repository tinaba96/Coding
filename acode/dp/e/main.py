import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict



N, W = list(map(int, input().split()))

#dp[i][w] i個まで選び、今の重さwの時の最大値

mp = []

for i in range(N):
    w, v = list(map(int, input().split()))
    mp.append((w, v))

dp = [defaultdict(int) for j in range(N+1)]
#dp = [[0 for i in range(W+1)] for j in range(N+1)]


def dynamic(ind, wei):
    if ind == N:
        return 
    nind = ind + 1
    nwei = wei
    #print(dp[ind][wei])
    dp[nind][nwei] = max(dp[nind][nwei], dp[ind][wei])
    dynamic(nind, nwei)
    if wei + mp[ind][0] <= W:
        nwei = wei + mp[ind][0]
        dp[nind][nwei] = max(dp[nind][nwei], dp[ind][wei] + mp[ind][1])
    dynamic(nind, nwei)

dynamic(0, 0)

ans = 0
for a in dp[N]:
    ans = max(ans, dp[N][a])

print(ans)



