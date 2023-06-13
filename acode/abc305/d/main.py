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
import bisect


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

slp = []
end = []
cum = [0]

for a in range(1, N):
    if a%2 == 1:
        slp.append(A[a])
        cum.append(cum[-1])
    else:
        end.append(A[a])
        cum.append(cum[-1] + A[a]-slp[-1])

#print(cum)


#dp = [0 for i in range(10**9+1)]

#dp[0] = 0

#print(slp)
#print(end)


for q in range(Q):
    val = 0
    l, r = list(map(int, input().split()))
    v = bisect.bisect_right(A, l)
    if v%2 == 0:
        val = A[v] - l
    v2 = bisect.bisect(A, r)
    if v2%2 == 0:
        val += r - A[v2-1]
    #print(cum)

    val += cum[v2-1] - cum[v]
    print(val)



