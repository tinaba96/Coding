import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import deque
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
ans  = 10**10

#print(len(need))

#memo = [[False for i in range()
memo = set()
# memo.add((43, 'sdf'))


def dfs(q):
    global ans
    global memo
    if not q:
        return

    #print('left: ', left)
    #print('seen: ', seen)
    #print('nd: ', nd)

    #if (left, seen) in memo: # zの値で評価できない
    #    return
    #print(q.popleft())

    left, ind, nd = q.popleft()

    if ind < N and smallest[ind][left] < nd:
        return

    if left <= 0:
        ans = min(ans, nd)
        #print(seen, ': ', nd)
        return

    d, z = need[i]

    if smallest[ind+1][left] > nd:
        q.append((left, ind+1, nd))
        smallest[ind+1][left] = nd

    if smallest[ind+1][left] > nd+d:
        q.append((left-z, ind+1, nd+d))
        smallest[ind+1][left] = nd+d

    #memo.add((left, seen))
    dfs(q)

smallest = [[10^10 for i in range(N)] for j in range(10^5+1)]

seen = [False]*(len(need)+1)
q = deque([])
q.append((dif, 0, 0))
dfs(q)

#dfs(dif, 0, 0)

print(ans)


# minをとってないということは計算すべき部分を飛ばしている？

# マス自体は100 x 10^5 だが、遷移がNあるため、全体の計算量は約O(10^5 * 100 * 100)  -> TLE


