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

cnta = 0
cntf = 0

N = int(input())
for i in range(N):
    S = str(input())
    if S == 'For':
        cntf += 1
    else:
        cnta += 1
if cntf > cnta:
    print('Yes')
else:
    print('No')





