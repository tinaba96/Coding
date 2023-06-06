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

for i in range(N):
    for j in range(i,N):
        a1 = all[i][0]
        a2 = all[i][1]
        b1 = all[j][0]
        b2 = all[j][1]
        #d = abs(a1-b1)**2 + abs(a2-b2)**2
        d = math.sqrt(abs(a1-b1)**2 + abs(a2-b2)**2)

        if d <= D:
            mp[i].append(j)
            mp[j].append(i)


#print(mp)
ans = [False for f in range(N)]

q = [0]

while q:
    v = q.pop()
    for g in range(len(mp[v])):

        nx = mp[v][g]
        if ans[nx] == True:
            continue
        else:
            #ans[nx] = True # this is AC
            q.append(nx)
    ans[v] = True  # this was the cause of TLE -> same value can be in the que so many times


#print(ans)

for a in ans:
    if a == True:
        print('Yes')
    else:
        print('No')


