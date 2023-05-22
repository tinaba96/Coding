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


N, M, D = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

import bisect

ans = -1

'''
for a in A:
    ind = bisect.bisect(B, a+D)
    if 
'''

indA = 0
indB = 0

while True:
    if A[indA] >= B[indB]:
        if A[indA]-B[indB] <=D:
            ans = max(ans, A[indA]+B[indB])
        if indB < M-1:
            indB += 1
        elif indA < N-1:
            indA += 1
    if A[indA] < B[indB]:
        if B[indB] - A[indA] <=D:
            ans = max(ans, A[indA]+B[indB])
        if indA < N-1:
            indA += 1
        elif indB < M-1:
            indB += 1
    if indA >= N-1 and indB >= M-1:
        break

print(ans)

# there is case that this approach will not work

