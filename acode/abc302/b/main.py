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
H, W = list(map(int, input().split()))


for i in range(H):
    S = str(input())
    mp.append(S)


ans = []

cand = []

for h in range(H):
    ans = []
    for w in range(W):
        if mp[h][w] == 's':
            cand.append((h, w))

move = [(0,1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (1, 0)]

target = 'snuke'

ind = 1

can = []

#print(cand)
ansmove = (0,0)

for h, w in cand:
    #print((h, w))
    x = h
    y = w
    for a, b in move:
        ind = 1
        h = x
        w = y
        for i in range(4):
            nh = h+a
            nw = w+b
            if nh<0 or nh > H-1 or nw < 0 or nw > W-1:
                break
            #print('a')
            if mp[nh][nw] == target[ind+i]:
                h = nh
                w = nw
                if ind+i == 4:
                    can = [(x+1, y+1), (h+1,w+1)]
                    ansmove = (a,b)
                continue
            else:
                break
    
j, d = ansmove
print(*can[0])
for q in range(1, 5):
    print(can[0][0]+ansmove[0]*q, can[0][1]+ansmove[1]*q)





