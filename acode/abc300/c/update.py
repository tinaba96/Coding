import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


H, W = list(map(int, input().split()))


mp = []

a = ''
for j in range(W):
    a += '.'

mp.append(a)

for h in range(H):
    C = str(input())
    c = '.'+C+'.'
    mp.append(c)

mp.append(a)

N = min(H, W)

ans = [0 for i in range(N)]

H += 2
W += 2

for h in range(2, H-2):
    for w in range(2, W-2):
        cnt = 0
        while True:
            if mp[h][w] != '#':
                break
            else:
                cnt += 1
                flg = True
                # no need to check 4 of them according to the explanation. see video editorial -> only need it to identify the center of the cross
                if mp[h-cnt][w-cnt] != '#':
                    flg = False
                    break
                if mp[h+cnt][w-cnt] != '#':
                    flg = False
                    break
                if mp[h-cnt][w+cnt] != '#':
                    flg = False
                    break
                if mp[h+cnt][w+cnt] != '#':
                    flg = False
                    break
        if cnt >= 2:
            ans[cnt-2] += 1


print(*ans)

