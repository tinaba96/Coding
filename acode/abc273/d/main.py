import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


H, W, rs, cs = list(map(int, input().split()))
N = int(input())

wal = set()
#row = [[] for v in range(10**9)]
#col = [[] for v in range(10**9)]

for n in range(N):
    r, c = list(map(int, input().split()))
    wal.add((r, c))
    #row[r].appen(c)
    #col[c].appen(r)

Q = int(input())

now = [rs, cs]
for q in range(Q):
    d, lstr = list(map(str, input().split()))
    l = int(lstr)
    if d == "U":
        defa = now[0]-l
        for f in range(1, l+1):
            if (now[0]-f, now[1]) in wal:
                print('yes')
                break
            now[0] -= f
        now = max(now[0]+1, defa)
    if d == "R":
        now[1] += l
        for ff in range(1, l+1):
            if (now[0], now[1]+ff) in wal:
                print('yes')
                now[1] += ff
                break
    if d == "L":
        now[1] -= l
        for fff in range(1, l+1):
            if (now[0], now[1]-fff) in wal:
                print('yes')
                now[1] -= fff
                break
    if d == "D":
        now[0] += l
        for ffff in range(1, l+1):
            if (now[0]+ffff, now[1]) in wal:
                print('yes')
                now[0] += ffff
                break
    print(now)




