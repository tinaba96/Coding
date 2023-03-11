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
    ix = x-1
    iy = y-1
    if (y,x) == (H, W):
        ans += 1
        return
    if y < H:
        if mp[iy+1][ix] in path:
            return
        path.add(mp[iy+1][ix])
        search(y+1, x, path)
        path.remove(mp[iy+1][ix])
    if x < W:
        if mp[iy][ix+1] in path:
            return
        path.add(mp[iy][ix+1])
        search(y, x+1, path)
        path.remove(mp[iy][ix+1])

path = set()

path.add(mp[0][0])

search(1, 1, path)

print(ans)

