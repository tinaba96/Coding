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
l = []
mp = []
mi = 10000000000000
ta = ''
flg = False
for i in range(N):
    n, a = list(map(str, input().split()))
    mp.append((n,a))
    if int(a) < mi:
        mi = int(a)

k = -1
ind = 0
for p, q in mp:
    if int(q) == mi:
        ta = p
        k = ind
    ind += 1


#print(l)
ans = []

ans = mp[k:] + mp[:k]

for i in range(len(ans)):
    print(ans[i][0])

