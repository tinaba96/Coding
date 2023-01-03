import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
A = list(map(int, input().split()))


Q = int(input())


for q in range(Q):
   qu = list(map(int, input().split()))
   if qu[0] == 1:
       A[qu[1]-1] = qu[2]
   else:
       print(A[qu[1]-1])





