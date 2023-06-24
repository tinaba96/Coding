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


A = list(map(int, input().split()))

ans = 0

for i in range(64):
    ans += A[i]<<i
    #ans += A[i]*(2<<i)

print(ans)


#print(345*2**64)
#print(345<<64)
