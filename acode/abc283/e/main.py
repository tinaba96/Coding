import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


H, W = list(map(int, input().split()))

mp = []

for i in range(H):
    A = list(map(int, input().split()))
    mp.append(A)

def indi(c, r, v):
    t = 1 - v
    if mp[c-1][r] == t and mp[c+1][r] == t and mp[c][r-1] == t and mp[c][r+1] == t:
        return True
    else:
        return False

listIndi = []

for h in range(H):
    for w in range(W):
        if indi(h, w, mp[h][w]):
            listIndi.append((h, w))

print(listIndi)




# DP?
