import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


H, W = list(map(int, input().split()))
cnt = 0
for i in range(H):
    s = str(input())
    for j in range(W):
        if s[j] == '#':
            cnt += 1
print(cnt)




