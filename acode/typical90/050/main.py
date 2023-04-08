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


N, L = list(map(int, input().split()))

mod = 10**9+7

st = [0 for i in range(N+1)]

st[0] = 1

for i in range(N):
    st[i+1] += st[i]
    if i+L < N+1:
        st[i+L] += st[i]

print(st[N] % mod)









