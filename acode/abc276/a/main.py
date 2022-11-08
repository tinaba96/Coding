import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


S = str(input())


ans = -1

for i in range(len(S)):
    if S[i] == 'a':
        ans = i+1

print(ans)



