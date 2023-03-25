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


A = str(input())


ind = 0
ans = 0

while True:
    if ind+1 >= len(A):
        break
    if A[ind] == A[ind+1]:
        ans += 1
        ind += 2
    else:
        ind += 1


