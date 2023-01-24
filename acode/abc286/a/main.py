import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, P, Q, R, S = list(map(int, input().split()))
A = list(map(int, input().split()))


ans = A[:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:]

print(*ans)

