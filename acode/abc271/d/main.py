import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, S = list(map(int, input().split()))

mp = []

for r in range(N):
    D = list(map(int, input().split()))
    mp.append(D)

dp = [[0 for i in range(2)] for j in range(S+1)]

# dp[残りの数][o, 1] = これまでのトータル

dp[0][0] = 0

for i in range(1, N):
    if S-mp[i-1][0] == 0:
        print("yes")
        exit()
    if S-mp[i-1][0] < 0:
        continue
    dp[S-mp[i-1][0]][0] = dp[i-1][0] + mp[i-1][0]
    dp[S-mp[i-1][1]][1] = dp[i-1][1] + mp[i-1][1]


print(dp)


