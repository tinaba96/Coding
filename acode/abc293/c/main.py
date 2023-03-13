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
    l = list(map(int, input().split()))
    mp.append(l)

#print(mp)
#print(mp[0][0])
ans = 0

def search(y, x, path):
    global ans
    if (y,x) == (H-1, W-1): #
    #if y == H-1 and x == W-1:
        ans += 1
    if y < H-1:
        if mp[y+1][x] in path:
            return
        path.add(mp[y+1][x])
        search(y+1, x, path)
        path.remove(mp[y+1][x])
    if x < W-1:
        if mp[y][x+1] in path:
            return
        path.add(mp[y][x+1])
        search(y, x+1, path)
        path.remove(mp[y][x+1])

path = set()

path.add(mp[0][0])

search(0, 0, path)

print(ans)

