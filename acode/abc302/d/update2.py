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

B.sort()

import bisect

ans = -1

for a in A:
    ind = bisect.bisect(B, a+D)
    if ind-1 >= 0 and B[ind-1] >= a-D and B[ind-1] - a <= D:
        ans = max(ans, B[ind-1] + a)


print(ans)


