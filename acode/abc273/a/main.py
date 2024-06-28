import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())

def f(k):
    if k == 0:
        return 1
    return k*f(k-1)

print(f(N))
