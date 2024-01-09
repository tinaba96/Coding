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


A, M, L, R = list(map(int, input().split()))

L -= A
R -= A

if L < 0 and 0 < R:
    rr = abs(R)//M
    ll = abs(L)//M
    print(rr+ll+1)
    exit()

if A <= L:
    amari = M-abs(L)%M
else:
    amari = M-abs(R)%M


if amari == M:
    print((R-L)//M+1)
    '''
    if R-L == 0:
        print((R-L)//M+1)
    else:
        print((R-L)//M)
    '''
else:
    g = R-L-amari
    if g < 0:
        print(0)
    elif g == 0:
        print(1)
    else:
        print(g//M+1)



