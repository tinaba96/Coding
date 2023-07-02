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

mp = []

N = int(input())

for i in range(N):
    x, y = list(map(int, input().split()))
    mp.append((x, y))

INF = 10**12+1

dp = [[0,0] for i in range(N+1)]

dp[0][0] = 0
dp[0][1] = 0

for i in range(N):
    Y = mp[i][1]
    #print(Y)
    #print(dp[0][1])
    if mp[i][0] == 0:
        #dp[i+1][0] = max(dp[i+1][0], dp[i][0]+Y)
        #dp[i+1][0] = max(dp[i+1][0], dp[i][1]+Y)
        dp[i+1][0] = max(dp[i][0], max(dp[i][0]+Y, dp[i][1]+Y))
        dp[i+1][1] = dp[i][1]
    if mp[i][0] == 1:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][1], dp[i][0]+Y)

#print(dp)
print(max(dp[N][0], dp[N][1]))




