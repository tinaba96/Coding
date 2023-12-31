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


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

if K == 1:
    print(0)
    exit()


l = [] 

for i in range(K-1):
    l.append(abs(A[i+1]-A[i]))

m = max(l)

index = 1
ans = 0
left = []

while index >= 1 and index <= K-2:
    if A[index] - A[index-1] < m and A[index+1] -A[index] < m:
        index += 1
        ans = A[index] - A[index-1]
    elif A[index+1] - A[index] == m:
        left.append(index)

    index += 1

print(m)
print(left)

print(ans)





