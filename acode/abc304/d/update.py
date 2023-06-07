import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict


W, H = list(map(int, input().split()))
N = int(input())
st = []

for i in range(N):
    p, q = list(map(int, input().split()))
    st.append((p,q))

mi = N
ma = 0

A = int(input())

x = list(map(int, input().split()))

B = int(input())

y = list(map(int, input().split()))

mpX = [[] for i in range(N+1)]
mpY = [0 for i in range(N+1)]

import bisect

for p,q in st:
    t = bisect.bisect(x,p)
    mpX[t].append(q)


cnt = 0
d = defaultdict(int)

for z in range(len(mpX)):
    for h in mpX[z]:
        t = bisect.bisect(y,h)
        d[t] += 1
        if d[t] > ma:
            ma = d[t]

    for c in d:
        cnt += 1
        if d[c] < mi:
            mi = d[c]
        #print(d[c])
    d = defaultdict(int)


if cnt < (A+1)*(B+1):
    mi = 0

print(mi, ma)






