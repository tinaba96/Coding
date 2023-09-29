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

l = len(need)

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

    #print(ind, left)
    #print(smallest)
    if ind < l and smallest[ind][left] < nd:
        dfs(q)
        return

    if left <= 0:
        ans = min(ans, nd)
        #print(seen, ': ', nd)
        dfs(q)
        return

    d, z = need[ind]

    if ind+1 == l:
        dfs(q)
        return

    if smallest[ind+1][left] > nd:
        q.append((left, ind+1, nd))
        smallest[ind+1][left] = nd

    if smallest[ind+1][left-z] > nd+d:
        q.append((left-z, ind+1, nd+d))
        smallest[ind+1][left-z] = nd+d

    #memo.add((left, seen))
    dfs(q)

smallest = [[10**10 for i in range(10**5+1)] for j in range(N)]

seen = [False]*(len(need)+1)
q = deque([])
d, z = need[0]
q.append((dif-z, 0, d))
q.append((dif, 0, 0))
#q.append((dif, 0, 0))
dfs(q)

#dfs(dif, 0, 0)

print(ans)
#print(q)


# minをとってないということは計算すべき部分を飛ばしている？

# マス自体は100 x 10^5 だが、遷移がNあるため、全体の計算量は約O(10^5 * 100 * 100)  -> TLE


