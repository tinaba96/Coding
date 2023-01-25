import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
S = str(input())

ans = []

for i in range(len(S)):
    ans.append(S[i])
    if i+1<len(S) and S[i] == 'n' and S[i+1] == 'a':
        ans.append('y')

print(''.join(ans))
