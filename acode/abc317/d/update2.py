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
#dif = (tot-1)//2 + 1
dif = (tot-1)//2 + 1 - tot_x

# dp[x] 残りxの時の値


dp = [10**6 for i in range(dif+1)]
dp[0] = 0
ans  = 10**6

#print(len(need))

#memo = [[False for i in range()
memo = set()
# memo.add((43, 'sdf'))


def dfs(left, seen, nd):
    global ans
    global memo

    #print('left: ', left)
    #print('seen: ', seen)
    #print('nd: ', nd)

    if (left, seen) in memo: # zの値で評価できない
        return

    if left <= 0:
        ans = min(ans, nd)
        return
    # for i in range(len(need)):
    for i in range(seen+1, len(need)):
        if i <= seen:
            continue

        d, z = need[i]

        #print(d, z)
        #dp[z] = min(dp[z], dp[i] + d)

        

        # 選ばないという選択肢
        #dfs(left, seen, nd)

        dfs(left-z, i, nd+d)

    memo.add((left, seen))


for i in range(len(need)):
    seen = [False]*(len(need)+1)
    dfs(dif, -1, 0)

#print(memo)
#print(dp)

print(ans)


'''
4
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
'''


# minをとってないということは計算すべき部分を飛ばしている？

# マス自体は100 x 10^5 だが、遷移がNあるため、全体の計算量は約O(10^5 * 100 * 100)


