import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
S = list(map(int, input().split()))

A = []
A.append(S[0])

for i in range(1, N):
    A.append(S[i]-S[i-1])

print(*A)




