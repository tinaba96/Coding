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


N, M = list(map(int, input().split()))

mp = []
for i in range(M):
    a = list(map(int, input().split()))
    mp.append(a)


re = [set() for i in range(N)]
#re = [defaultdict(int) for i in range(M)] # if you use dict, you need key and val

for s in range(N):
    for l in range(N):
        re[l].add(s+1)

for m in range(M):
    for n in range(N-1):
        left = mp[m][n]
        right = mp[m][n+1]
        if right in re[left-1]:
            re[left-1].remove(right)
        if left in re[right-1]:
            re[right-1].remove(left)

#print(re)


ans = -N
for i in range(len(re)):
    ans += len(re[i])

ans = ans // 2

print(ans)


