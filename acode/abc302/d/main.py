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


N, M, D = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

import bisect

ans = -1

for a in A:
    ind_st = bisect.bisect(B, a)
    ind = bisect.bisect(B, a+D)
    #print(ind_st)
    if ind_st < len(B) and B[ind_st] >= a and B[ind_st] - a <= D:
        ans = max(ans, B[ind_st] + a)
    if ind < len(B) and B[ind] >= a and B[ind] - a <= D:
        ans = max(ans, B[ind] + a)
    if ind-1 >= 0 and B[ind-1] >= a and B[ind-1] - a <= D:
        ans = max(ans, B[ind-1] + a)

for b in B:
    ind_st = bisect.bisect(A, b)
    ind = bisect.bisect(A, b+D)
    #print(ind_st)
    if ind_st < len(A) and A[ind_st] >= b and A[ind_st] - b <= D:
        ans = max(ans, A[ind_st] + b)
    if ind < len(A) and A[ind] >= b and A[ind] - b <= D:
        ans = max(ans, A[ind] + b)
    if ind-1 >= 0 and A[ind-1] >= b and A[ind-1] - b <= D:
        ans = max(ans, A[ind-1] + b)

print(ans)

