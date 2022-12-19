import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


S = str(input())
T = str(input())

for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        exit()
print(len(S)+1)



