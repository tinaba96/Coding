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
A = list(map(int, input().split()))

ans = []
e = set(A)

tmp = []

for i in range(N):
    if i+1 not in e:
        ans.append(i+1)
        for t in range(len(tmp)):
            ans.append(tmp[-t-1])
        tmp = []
    else:
        tmp.append(i+1)

print(*ans)



