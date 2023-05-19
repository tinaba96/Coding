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


N, P, Q = list(map(int, input().split()))
A = list(map(int, input().split()))


A = [e%P for e in A]

c = Counter(A)

#print(A)
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                v = A[i]*A[j]*A[l]*A[k] % P
                key = (Q//v)%P



print(ans)


