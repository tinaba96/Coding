import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


S = str(input())
cnt = 0

for i in range(len(S)):
    if S[i] == 'v':
        cnt += 1
    else:
        cnt += 2

print(cnt)
