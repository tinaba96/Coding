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

ans = 0
if K%2 == 0:
    for i in range(0, K, 2):
        ans += A[i+1]-A[i]

    print(ans)
    exit()


base = 0
for i in range(0, K-1, 2):
    base += A[i+1]-A[i]

print(base)


ans = min(base, base-(A[1]-A[0])+(A[K-1]-A[K-2]))
print(base)

for i in range(1, K-2):
    if i == K-2:
        minus = A[i]-A[i-1]
        plus = A[K-1] - A[K-3]
    else:
        minus = A[i+1]-A[i] + A[i]-A[i-1]
        plus = A[K-1] - A[K-2]
    ans = min(ans, base-minus+plus)



print(ans)
    
