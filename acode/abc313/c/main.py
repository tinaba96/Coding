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
A = list(map(int, input().split()))


t = sum(A)

m = t//N
nm = m+1

cnt = 0
mi = 0
pl = 0

for i in range(N):
    if A[i] < m:
        mi += m-A[i]
        cnt += m-A[i]
    elif A[i] > nm:
        pl += A[i] - nm
        cnt += A[i] - nm

print(max(mi, pl))

#print(cnt)
'''
if cnt%2 != 0:
    print((cnt+1)//2)
else:
    print(cnt//2)
'''

