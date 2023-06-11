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


H, W = list(map(int, input().split()))

mp = []

for h in range(H):
    S = str(input())
    mp.append(S)

x = []
y = []

for h in range(H):
    for w in range(W):
        if mp[h][w] == '#':
            x.append(h)
            y.append(w)
            #print(h, w)

cntX = Counter(x)
cntY = Counter(y)

#print(cntX)
#print(cntY)


c1 = cntX[0]
c2 = cntX[1]

if len(cntX) >= 3 and len(cntY) >= 3:
    ansX = []

    for e in cntX:
        ansX.append(cntX[e])

    ansY = []
    for e in cntY:
        ansY.append(cntY[e])

    ansX.sort()
    ansY.sort()
    lx = len(ansX)
    xV = 0
    if ansX[0] != ansX[1]:
        xV = ansX[0]
    if ansX[lx-2] != ansX[lx-1]:
        xV = ansX[lx-1]

    ly = len(ansY)
    yV = 0
    if ansY[0] != ansY[1]:
        yV = ansY[0]
    if ansY[ly-2] != ansY[ly-1]:
        yV = ansX[ly-1]

#print(xV)
    ans1 = 0
    ans2 = 0

    for i in cntX:
        if cntX[i] == xV:
            ans1 = i

    for i in cntY:
        if cntY[i] == yV:
            ans2 = i

    print(ans1+1, ans2+1)

else:
    x.sort()
    y.sort()

    sx = min(x)
    ex = max(x)

    sy = min(y)
    ey = max(y)

    #print(sx, ex)
    #print(sy, ey)


    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            if mp[i][j] != '#':
                print(i+1, j+1)
                exit()

