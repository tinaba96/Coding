import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
A = list(map(int, input().split()))

ma = A[0]
ans = 1
for i in range(N-1):
    if ma < A[i+1]:
        ma = A[i+1]
        ans = i+2
print(ans)



