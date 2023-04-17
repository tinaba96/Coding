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


Q = int(input())
S ='1'
for q in range(Q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        c = str(x[1])
        S += c
        if len(S) > 10**10:
            i = int(S)
            S = str(i%998244353)
    if x[0] == 2:
        S = S[1:]
    if x[0] == 3:
        i = int(S)
        print(i%998244353)



