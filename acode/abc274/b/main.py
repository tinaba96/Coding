import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


H, W = list(map(int, input().split()))

ans = [0 for i in range(W)]

for j in range(H):
    C = str(input())
    #print(C)
    for k in range(W):
        if C[k] == "#":
            ans[k] += 1


print(*ans)

