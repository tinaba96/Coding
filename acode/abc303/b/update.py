import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict


N, M = list(map(int, input().split()))

mp = []
for i in range(M):
    a = list(map(int, input().split()))
    mp.append(a)

re = [set() for i in range(N)]

for s in range(N):
    for l in range(N):
        re[l].add(s+1)


for m in range(M):
    for n in range(N-1):
        left = mp[m][n]
        right = mp[m][n+1]
        re[left-1].discard(right)
        re[right-1].discard(left)

#print(re)


ans = -N
for i in range(len(re)):
    ans += len(re[i])

ans = ans // 2

print(ans)


# discard() will not throw an error even if there is no val

