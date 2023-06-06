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


N, D = list(map(int, input().split()))

all = []

for i in range(N):
    x, y = list(map(int, input().split()))
    all.append((x, y))

import math

mp = [[] for _ in range(N)]


#print(mp)
ans = [False for f in range(N)]

q = [0]
ans[0] = True

while q:
    v = q.pop()

    for i in range(len(all)):
        if ans[i] == True:
            continue
        a1 = all[v][0]
        a2 = all[v][1]
        b1 = all[i][0]
        b2 = all[i][1]
        d = math.sqrt(abs(a1-b1)**2 + abs(a2-b2)**2)

        if d <= D:
            q.append(i)
            ans[i] = True


#print(ans)

for a in ans:
    if a == True:
        print('Yes')
    else:
        print('No')


