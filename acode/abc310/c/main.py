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


N = int(input())

se = set()

import math
cnt = 0

for s in range(N):
    S = str(input())
    if S == S[::-1] and S not in se:
        cnt += 1

    se.add(S)
    se.add(S[::-1])

#print(se)
print((len(se)+cnt)//2)

#print(math.ceil((len(se)+cnt)/2))
#print(len(se)//2)

