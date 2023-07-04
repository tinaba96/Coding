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
    s = str(input())
    mp.append(s)

sn = 'snuke'
memo = set()

def search(i, h, w):
    if (i, h, w) in memo:
        return False
    if h >= H or w >= W or h < 0 or w < 0 or sn[i%5] != mp[h][w]:
        return False

    #print(i, h, w)
    ni = (i+1)%5

    if h == H-1 and w == W-1:
        print('Yes')
        exit()
    
    if search(ni, h+1, w) == False:
        memo.add((ni, h+1, w))
    if search(ni, h, w+1) == False:
        memo.add((ni, h, w+1))
    if search(ni, h-1, w) == False:
        memo.add((ni, h-1, w))
    if search(ni, h, w-1) == False:
        memo.add((ni, h, w-1))
    #search(i+1, h, w+1)
    #search(i+1, h-1, w)
    #search(i+1, h, w-1)
    if search(ni, h+1, w) == False and search(ni, h, w+1) == False and search(ni, h-1, w) == False and search(ni, h, w-1) == False:
        memo.add((i, h, w))



search(0, 0, 0)

print('No')

