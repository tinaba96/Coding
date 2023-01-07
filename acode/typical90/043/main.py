import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


H, W = list(map(int, input().split()))
rs, cs = list(map(int, input().split()))
rt, ct = list(map(int, input().split()))

mp = []

for i in range(H):
    s = str(input())
    mp.append(s)

ans = 100100100

v = [[0, 1], [0, -1], [-1, 0], [1, 0]] #di



def dfs(r, c, di, cnt):
    print(r, c)
    print(mp[r-1][c-1])

    if r <= 0 or c <= 0 or r > W or c > H or mp[r-1][c-1] == '#':
        return
    if r == rt and c == ct:
        print(cnt)
        exit()
    for d in range(4):
        print('ch: ', d)
        nr = r + v[d][0]
        nc = c + v[d][1]
        if di == d:
            dfs(nr, nc, d, cnt)
        else:
            dfs(nr, nc, d, cnt+1)
    return

dfs(rs, cs, 3, 0)





    




