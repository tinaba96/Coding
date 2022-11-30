import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, Q = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(set)


for i in range(Q):
    T, A, B = list(map(int, input().split()))
    if T == 1:
        d[A].add(B)
    if T == 2:
        if B in d[A]:
            d[A].remove(B)
    if T == 3:
        if B in d[A] and A in d[B]:
            print('Yes')
        else:
            print('No')


#print(d)



