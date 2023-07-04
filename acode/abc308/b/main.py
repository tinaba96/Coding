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


N, M = list(map(int, input().split()))
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

ans = 0

for p in C:
    if p not in D:
        ans += P[0]
    else:
        ind = D.index(p)
        ans += P[1+ind]
   # print(ind)

print(ans)
