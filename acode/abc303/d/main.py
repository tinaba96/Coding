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


X, Y, Z = list(map(int, input().split()))
S = str(input())

N = len(S)

dp = [[0,0] for i in range(N)]

if S[0] == 'A':
    dp[0][0] = Z+X # ON
    dp[0][1] = Y # OFF
else:
    dp[0][0] = Z+Y # ON
    dp[0][1] = X # OFF


for j in range(1, N):
    if S[j] == 'A':
        dp[j][0] = min(dp[j-1][0]+X, dp[j-1][1]+Z+X)
        dp[j][1] = min(dp[j-1][0]+Z+Y, dp[j-1][1]+Y)
    else:
        dp[j][0] = min(dp[j-1][0]+Y, dp[j-1][1]+Z+Y)
        dp[j][1] = min(dp[j-1][0]+Z+X, dp[j-1][1]+X)

print(min(dp[N-1]))





