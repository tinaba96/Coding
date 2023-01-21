import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

import bisect
import itertools

N = int(input())
A = list(map(int, input().split()))


# this is DP?

def calc(holi, num):
    val = 0
    for i in range(N):
        ind = bisect.bisect(holi, i)
        x = A[ind-1]
        y = A[ind]
        val += A[min(x, y)-1] # -i is for index


calc([1,4], 2)

# how dicide the numbe of holiday



