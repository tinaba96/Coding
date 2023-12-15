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

S = str(input())
T = str(input())

ans = 3

if T[:N] == S:
    ans -= 2

if T[M-N:] == S:
    ans -= 1

#if T[:N] == S and T[N+1:] == S:
#    ans -= 1

print(ans)


