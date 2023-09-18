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
        need.append(((Y-X)//2+1, Z))

if tot_x > tot-tot_x:
    print(0)
    exit()

tot_y = tot-tot_x
#dif = tot_y - tot_x

#dif = tot//2 + 1
dif = (tot-1)//2 + 1

# dp[x] 残りxの時の値


dp = [10**6 for i in range(dif+1)]
dp[0] = 0
ans  = 10**6

print(len(need))

def dfs(left, seen, nd):
    global ans
    print('left: ', left)
    print('seen: ', seen)
    print('nd: ', nd)
    if left <= 0:
        ans = min(ans, nd)
        return
    for i in range(len(need)):
        if seen[i] == True:
            continue

        seen[i] = True
        d, z = need[i]

        #print(d, z)
        #dp[z] = min(dp[z], dp[i] + d)

        # 選ばないという選択肢
        dfs(left, seen, nd)

        dfs(left-z, seen, nd+d)
        seen[i] = False

for i in range(len(need)):
    seen = [False]*(len(need)+1)
    dfs(dif, seen, 0)

#print(dp)
print(ans)


# 実装しきれんかった、、計算量もOK?
'''
4
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
'''

# 動作を一から確認する。


