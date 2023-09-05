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


N = int(input())

mp = [[] for i in range(N+1)]

for i in range(N):
    F, S = list(map(int, input().split()))
    mp[F].append(S)

ans = 0
top = []
for i in range(N+1):
    mp[i].sort(reverse=True)
    if len(mp[i]) > 0:
        top.append(mp[i][0])

top.sort(reverse=True)
#print(mp)
#print(top)
if len(top) > 1:
    ans = top[0]+top[1]

for i in range(N+1):
    if len(mp[i]) > 1:
        v = mp[i][0] + mp[i][1]//2
        ans = max(ans, v)

print(ans)


