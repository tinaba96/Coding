import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())

ans = str.upper(str(hex(N))[2:])
if len(ans) == 1:
    print('0'+ans)
else:
    print(ans)


