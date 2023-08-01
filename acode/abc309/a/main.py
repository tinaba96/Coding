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


A, B = list(map(int, input().split()))

c = [2, 5, 8]

if A not in c and B not in c:
    print('No')
    exit()

if B-A == 1:
    print('Yes')
else:
    print('No')



