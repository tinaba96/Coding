import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
A = list(map(int, input().split()))


ans = [0 for i in range(2*N+1)]

for j in range(N):
    #print(j, ' ', A[j])
    ans[2*(j+1)-1] = ans[A[j]-1] + 1
    ans[2*(j+1)] = ans[A[j]-1] + 1

for a in ans:
    print(a)

