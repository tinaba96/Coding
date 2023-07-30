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

mp = []
FF = []

N, M = list(map(int, input().split()))

for i in range(N):
    P, C, *F = list(map(int, input().split()))

    mp.append((P, C))
    F = set(F)
    FF.append(F)

ans = 'No'

for p in range(N):
    for q in range(N):
        if mp[p][0] >= mp[q][0]:
            if (mp[p][0] > mp[q][0] or len(FF[p]) < len(FF[q])) and FF[p] <= FF[q]:
                ans = 'Yes'
                print(ans)
                exit()
            else:
                continue

print(ans)
