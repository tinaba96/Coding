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


N, M = list(map(int, input().split()))

mp = [[] for i in range(N)]
ind = [[] for i in range(N)]

#mp[0].append(0)
#ind[0].append((0,0))

for i in range(M):
    A, B, X, Y = list(map(int, input().split()))
    if B < A:
        A, B = B, A
        X = -X
        Y = -Y
    mp[A-1].append(B-1)
    ind[A-1].append((X, Y))


ans = [[] for i in range(N)]
ans[0] = (0,0)

#print('mp: ', mp)
#print('ind: ', ind)

for i in range(N):
    for j in range(len(mp[i])):
        #print(ans)
        t = mp[i][j]
        nx = ind[i][j][0]
        ny = ind[i][j][1]
        if ans[i] == []:
            continue
        ans[mp[i][j]] = (ans[i][0]+nx, ans[i][1]+ny)


for i in range(len(ans)):
    if ans[i] == []:
        print('undecidable')
    else:
        print(*ans[i])



# 上記のような順方向のみでは、下記のようなケースで落ちる。
# 1 -> 3, 2 -> 3 の場合、2も3から求めらるべき。
# よって、双方向から探索する必要がある。
# 解説動画で質問→回答済み。










