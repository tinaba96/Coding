import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

A, B, C, D, E, F = list(map(int, input().split()))

left = A*B*C
right = D*E*F

print((left-right)%998244353)

