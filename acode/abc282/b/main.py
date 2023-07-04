import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))

mp = []

for i in range(N):
    S = str(input())
    mp.append(S)
ans = 0
for p in range(N):
    for q in range(p+1, N):
        flg = True
        for c in range(M):
            if mp[p][c] == 'x' and mp[q][c] == 'x':
                flg = False
        if flg:
            ans += 1



print(ans)



