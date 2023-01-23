import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
d = defaultdict(int)


N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

num2 = 0

for a in range(len(A)):
    d[a] = A[a]


for i in range(Q):
    T, x, y = list(map(int, input().split()))
    if T == 1:
        d[(x-1-num2)%N], d[(y-1-num2)%N] = d[(y-1-num2)%N], d[(x-1-num2)%N]
        #tmp = d[x]
        #d[x] = d[y]
        #d[y] = tmp

    if T == 2:
        num2 += 1
    if T == 3:
        print(d[(x-1-num2)%N])

#print(-3%7)







