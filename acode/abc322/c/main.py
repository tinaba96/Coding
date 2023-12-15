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

import bisect


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(1, N+1):
    ind = bisect.bisect_left(A, i)
    #v = min(abs(i-A[ind]), abs(i-A[ind-1]))
    v = A[ind] - i
    print(v)

