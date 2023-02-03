import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N, K = list(map(int, input().split()))

mp = []

for i in range(N):
    A, B = list(map(int, input().split()))
    mp.append((A,B))

dp = [[0 for x in range(K+1)] for z in range(N+1)]
# dp[p][q] pまでみた時の残りq分
dp[0][K] = 0


for k in range(N):
    nk = k+1
    for j in range(K+1):
        dp[nk][j] = max(dp[nk][j], dp[k][j])
        if j-1 >= 0:
            dp[nk][j-1] = max(dp[nk][j-1], dp[k][j]+mp[k][1]) # part
        if j-2 >= 0:
            dp[nk][j-2] = max(dp[nk][j-2], dp[k][j]+mp[k][0]) # full

print(dp[N][0])





