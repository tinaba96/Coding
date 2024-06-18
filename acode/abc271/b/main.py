import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, Q = list(map(int, input().split()))

mp = []

for i in range(N):
    L = list(map(int, input().split()))
    mp.append(L)

for k in range(Q):
    s, t = list(map(int, input().split()))
    print(mp[s-1][t])





