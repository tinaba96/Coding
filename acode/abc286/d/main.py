import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


from collections import defaultdict
d = defaultdict(int)


N, X = list(map(int, input().split()))

mp = [] 

for k in range(N):
    A, B = list(map(int, input().split()))
    d[A] = B
    for p in range(B):
        mp.append(A)


# dp[i][j] i版目まで見て残りj

dp = [[False for i in range(10010)] for j in range(10010)] #this is to big

dp[0][0] = True

for i in range(1, N+1):
    for j in range(X+1):
        if dp[i-1][j] == True:
            if j-mp[i-1] < 0:
                break
            dp[i][j-mp[i-1]] = True

for a in range(N+1):
    print(dp[a][0])



