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


tot = 0
tot_x = 0
N = int(input())
need = []

for i in range(N):
    X, Y, Z = list(map(int, input().split()))
    tot += Z
    if X > Y:
        tot_x += Z
    else:
        need.append((Y-X, Z))

if tot_x > tot-tot_x:
    print(0)
    exit()

tot_y = tot-tot_x
dif = tot_y - tot_x

# dp[x] 残りxの時の値


dp = [10**6 for i in range(dif+1)]
dp[0] = 0


for i in range(len(need)):
    d, z = need[i]
    dp[z] = min(dp[z], dp[i] + d)


print(dp)

