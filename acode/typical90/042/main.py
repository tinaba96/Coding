import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


K = int(input())



val = 1

while val <= 10**K:
    val *= 9

MOD = 10**9+7

dp = [0 for p in range(K+10)]

dp[1] = 0

for i in range(2, K+1):
    for t in range(1, 9):

        if (i + t)% 9 == 0:
            dp[i+t] += dp[i]
            dp[i+t] %= MOD
            dp[i+t] += 1


print(dp)
print(dp[-2])





